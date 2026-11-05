"""
========================================================================================
CSA1714 - Artificial Intelligence | Course Outcome 1 (CO1)
Assignment 1: Autonomous Hospital Medicine-Delivery Robot Uninformed Search Strategy
Student Name: Bhuvanesh H
Register No: 192524027
Institution: Department of Computer Science & Engineering
========================================================================================
"""

import time
import random
import heapq
from collections import deque
from typing import Dict, List, Tuple, Set, Optional, Any

# ======================================================================================
# 1. HOSPITAL WARD TOPOLOGY GENERATOR
# ======================================================================================

def generate_hospital_graph(num_states: int, branching_target: int = 3, seed: int = 42) -> Dict[int, List[Tuple[int, int]]]:
    """
    Generates a realistic multi-floor hospital graph with branching factor ~3.
    Edges are weighted by transit traversal costs (e.g., corridor length, ramp incline).
    """
    random.seed(seed)
    adj: Dict[int, List[Tuple[int, int]]] = {i: [] for i in range(num_states)}
    
    # 1. Tree backbone guaranteeing global reachability
    for i in range(1, num_states):
        parent = random.randint(max(0, i - 15), i - 1)
        cost = random.randint(1, 5)
        adj[parent].append((i, cost))
        adj[i].append((parent, cost))
        
    # 2. Add cross corridors, bypasses, and elevator links
    for _ in range(num_states // 2):
        u = random.randint(0, num_states - 1)
        v = random.randint(max(0, u - 10), min(num_states - 1, u + 10))
        if u != v and not any(nbr == v for nbr, _ in adj[u]):
            cost = random.randint(1, 5)
            adj[u].append((v, cost))
            adj[v].append((u, cost))
            
    return adj

# ======================================================================================
# 2. UNINFORMED SEARCH STRATEGIES
# ======================================================================================

def breadth_first_search(adj: Dict[int, List[Tuple[int, int]]], start: int, goal: int) -> Dict[str, Any]:
    """Breadth-First Search (FIFO queue). Finds shallowest step-count path."""
    queue = deque([start])
    visited: Dict[int, Optional[int]] = {start: None}
    nodes_expanded = 0
    nodes_generated = 1
    max_frontier = 1
    t0 = time.perf_counter()
    
    found = False
    while queue:
        max_frontier = max(max_frontier, len(queue))
        curr = queue.popleft()
        nodes_expanded += 1
        
        if curr == goal:
            found = True
            break
            
        for nbr, _ in adj.get(curr, []):
            if nbr not in visited:
                visited[nbr] = curr
                nodes_generated += 1
                queue.append(nbr)
                
    t1 = time.perf_counter()
    
    path = []
    if found:
        c = goal
        while c is not None:
            path.append(c)
            c = visited[c]
        path.reverse()
        
    return {
        "algorithm": "BFS",
        "found": found,
        "path_length": len(path) - 1 if found else -1,
        "nodes_expanded": nodes_expanded,
        "nodes_generated": nodes_generated,
        "max_frontier": max_frontier,
        "runtime_sec": t1 - t0,
        "path": path
    }

def uniform_cost_search(adj: Dict[int, List[Tuple[int, int]]], start: int, goal: int) -> Dict[str, Any]:
    """Uniform-Cost Search (Priority queue keyed by cumulative edge cost g(n))."""
    pq: List[Tuple[int, int]] = [(0, start)]
    cost_so_far: Dict[int, int] = {start: 0}
    parent: Dict[int, Optional[int]] = {start: None}
    nodes_expanded = 0
    nodes_generated = 1
    max_frontier = 1
    t0 = time.perf_counter()
    
    found = False
    while pq:
        max_frontier = max(max_frontier, len(pq))
        cost, curr = heapq.heappop(pq)
        nodes_expanded += 1
        
        if curr == goal:
            found = True
            break
            
        if cost > cost_so_far[curr]:
            continue
            
        for nbr, w in adj.get(curr, []):
            new_cost = cost + w
            if nbr not in cost_so_far or new_cost < cost_so_far[nbr]:
                cost_so_far[nbr] = new_cost
                parent[nbr] = curr
                nodes_generated += 1
                heapq.heappush(pq, (new_cost, nbr))
                
    t1 = time.perf_counter()
    
    path = []
    if found:
        c = goal
        while c is not None:
            path.append(c)
            c = parent[c]
        path.reverse()
        
    return {
        "algorithm": "UCS",
        "found": found,
        "total_cost": cost_so_far.get(goal, -1),
        "path_length": len(path) - 1 if found else -1,
        "nodes_expanded": nodes_expanded,
        "nodes_generated": nodes_generated,
        "max_frontier": max_frontier,
        "runtime_sec": t1 - t0,
        "path": path
    }

def depth_limited_search(adj: Dict[int, List[Tuple[int, int]]], start: int, goal: int, limit: int) -> Dict[str, Any]:
    """Depth-Limited Search helper with recursive path-set cycle check."""
    nodes_expanded = [0]
    nodes_generated = [1]
    max_depth = [0]
    
    def recursive_dls(node: int, depth: int, path_set: Set[int]) -> Any:
        nodes_expanded[0] += 1
        max_depth[0] = max(max_depth[0], depth)
        
        if node == goal:
            return [node]
        if depth >= limit:
            return 'cutoff'
            
        cutoff_occurred = False
        for nbr, _ in adj.get(node, []):
            if nbr not in path_set:
                nodes_generated[0] += 1
                path_set.add(nbr)
                res = recursive_dls(nbr, depth + 1, path_set)
                path_set.remove(nbr)
                if res == 'cutoff':
                    cutoff_occurred = True
                elif res is not None:
                    return [node] + res
        return 'cutoff' if cutoff_occurred else None

    t0 = time.perf_counter()
    path_result = recursive_dls(start, 0, {start})
    t1 = time.perf_counter()
    
    return {
        "found": isinstance(path_result, list),
        "cutoff": path_result == 'cutoff',
        "nodes_expanded": nodes_expanded[0],
        "nodes_generated": nodes_generated[0],
        "max_depth": max_depth[0],
        "runtime_sec": t1 - t0,
        "path": path_result if isinstance(path_result, list) else []
    }

def iterative_deepening_dfs(adj: Dict[int, List[Tuple[int, int]]], start: int, goal: int, max_limit: int = 30) -> Dict[str, Any]:
    """Iterative Deepening Depth-First Search. Combines linear memory O(bd) with completeness."""
    total_expanded = 0
    total_generated = 0
    max_frontier_depth = 0
    t0 = time.perf_counter()
    
    final_path = []
    found = False
    for limit in range(max_limit):
        res = depth_limited_search(adj, start, goal, limit)
        total_expanded += res["nodes_expanded"]
        total_generated += res["nodes_generated"]
        max_frontier_depth = max(max_frontier_depth, res["max_depth"])
        if res["found"]:
            found = True
            final_path = res["path"]
            break
            
    t1 = time.perf_counter()
    return {
        "algorithm": "IDDFS",
        "found": found,
        "path_length": len(final_path) - 1 if found else -1,
        "nodes_expanded": total_expanded,
        "nodes_generated": total_generated,
        "max_frontier": max_frontier_depth,
        "runtime_sec": t1 - t0,
        "path": final_path
    }

# ======================================================================================
# 3. DAY-4 DESIGN CHALLENGE: SENSOR UNCERTAINTY & BELIEF STATE GRAPH SEARCH
# ======================================================================================

def belief_state_search(junction_transitions: Dict[str, Dict[str, List[str]]],
                        initial_belief: Set[str],
                        goal_state: str) -> Dict[str, Any]:
    """
    Belief State Search under Sensor Failure (Partially Observable Junction Navigation).
    States in belief state B expand deterministically into new belief sets:
    B' = Union_{s in B} Succ(s, a).
    Goal is reached when all possible robot physical states in B are subset of goal.
    """
    initial_b = frozenset(initial_belief)
    frontier = deque([(initial_b, [])])
    visited = {initial_b}
    
    expanded_count = 0
    actions = ["GoStraight", "TurnLeft", "TurnRight"]
    
    while frontier:
        b, plan = frontier.popleft()
        expanded_count += 1
        
        # Check if belief state is goal-satisfied
        if all(s == goal_state for s in b):
            return {
                "success": True,
                "plan": plan,
                "belief_states_expanded": expanded_count,
                "final_belief": set(b)
            }
            
        for act in actions:
            next_b_set = set()
            for s in b:
                successors = junction_transitions.get(s, {}).get(act, [s])
                for succ in successors:
                    next_b_set.add(succ)
            
            f_next_b = frozenset(next_b_set)
            if f_next_b not in visited and f_next_b:
                visited.add(f_next_b)
                frontier.append((f_next_b, plan + [act]))
                
    return {"success": False, "plan": [], "belief_states_expanded": expanded_count}

# ======================================================================================
# 4. BENCHMARK RUNNER & DEMONSTRATION
# ======================================================================================

if __name__ == "__main__":
    print("=" * 75)
    print("CSA1714 Assignment 1: Uninformed Search Strategy Benchmarking")
    print("Student: Bhuvanesh H (192524027)")
    print("=" * 75)
    
    for state_count in [1000, 10000, 50000]:
        print(f"\n--- Testing Hospital Topology with {state_count:,} Ward Intersections ---")
        graph = generate_hospital_graph(state_count, seed=42)
        start_node = 0
        goal_node = state_count - 5
        
        r_bfs = breadth_first_search(graph, start_node, goal_node)
        r_ucs = uniform_cost_search(graph, start_node, goal_node)
        r_iddfs = iterative_deepening_dfs(graph, start_node, goal_node, max_limit=20)
        
        print(f"BFS   : Expanded={r_bfs['nodes_expanded']:6d} | MaxFrontier={r_bfs['max_frontier']:6d} | Time={r_bfs['runtime_sec']:.4f}s | PathLen={r_bfs['path_length']}")
        print(f"UCS   : Expanded={r_ucs['nodes_expanded']:6d} | MaxFrontier={r_ucs['max_frontier']:6d} | Time={r_ucs['runtime_sec']:.4f}s | Cost={r_ucs['total_cost']}")
        print(f"IDDFS : Expanded={r_iddfs['nodes_expanded']:6d} | MaxDepthStack={r_iddfs['max_frontier']:4d} | Time={r_iddfs['runtime_sec']:.4f}s | PathLen={r_iddfs['path_length']}")
        
    print("\n--- Day-4 Design Challenge: Belief State Search Demonstration ---")
    junction_rules = {
        "Junction_North": {"GoStraight": ["ICU_Room"], "TurnLeft": ["Corridor_A"], "TurnRight": ["Storage_B"]},
        "Junction_South": {"GoStraight": ["ICU_Room"], "TurnLeft": ["Storage_B"], "TurnRight": ["Corridor_A"]},
    }
    uncertain_belief = {"Junction_North", "Junction_South"}
    res_belief = belief_state_search(junction_rules, uncertain_belief, "ICU_Room")
    print(f"Initial Uncertain Belief : {uncertain_belief}")
    print(f"Conformant Action Plan   : {res_belief['plan']}")
    print(f"Belief States Expanded   : {res_belief['belief_states_expanded']}")
    print(f"Final Belief Target      : {res_belief['final_belief']}")
    print("=" * 75)
