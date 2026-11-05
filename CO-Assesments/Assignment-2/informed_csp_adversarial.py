"""
========================================================================================
CSA1714 - Artificial Intelligence | Course Outcome 2 (CO2)
Assignment 2: Informed Search, CSP, Adversarial Search, and Combinatorial Optimization
Student Name: Bhuvanesh H
Register No: 192524027
Institution: Department of Computer Science & Engineering
========================================================================================
"""

import time
import random
import heapq
import itertools
from collections import deque
from typing import Dict, List, Tuple, Set, Optional, Any

# ======================================================================================
# TASK 1: INFORMED SEARCH (UCS vs GREEDY BEST-FIRST vs A*)
# ======================================================================================

def manhattan_distance(a: Tuple[int, int], b: Tuple[int, int]) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def search_grid(grid: List[List[int]], start: Tuple[int, int], goal: Tuple[int, int], mode: str = 'astar') -> Dict[str, Any]:
    rows, cols = len(grid), len(grid[0])
    h0 = manhattan_distance(start, goal)
    f0 = h0 if mode == 'greedy' else (0 if mode == 'ucs' else h0)
    
    pq = [(f0, 0, start)]
    cost_so_far = {start: 0}
    parent: Dict[Tuple[int, int], Optional[Tuple[int, int]]] = {start: None}
    nodes_expanded = 0
    nodes_generated = 1
    max_frontier = 1
    t0 = time.perf_counter()

    while pq:
        max_frontier = max(max_frontier, len(pq))
        f, g, curr = heapq.heappop(pq)
        nodes_expanded += 1
        
        if curr == goal:
            break
            
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = curr[0] + dr, curr[1] + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                new_g = g + 1
                nbr = (nr, nc)
                if nbr not in cost_so_far or new_g < cost_so_far[nbr]:
                    cost_so_far[nbr] = new_g
                    parent[nbr] = curr
                    nodes_generated += 1
                    h = manhattan_distance(nbr, goal)
                    f_nbr = new_g if mode == 'ucs' else (h if mode == 'greedy' else new_g + h)
                    heapq.heappush(pq, (f_nbr, new_g, nbr))
                    
    t1 = time.perf_counter()
    path = []
    if goal in cost_so_far:
        c = goal
        while c is not None:
            path.append(c)
            c = parent[c]
        path.reverse()
        
    return {
        "mode": mode.upper(),
        "path_length": len(path) - 1 if path else -1,
        "cost": cost_so_far.get(goal, -1),
        "expanded": nodes_expanded,
        "generated": nodes_generated,
        "frontier": max_frontier,
        "runtime_sec": t1 - t0
    }

# ======================================================================================
# TASK 3: ALPHA-BETA PRUNING & MOVE ORDERING
# ======================================================================================

class AlphaBetaEngine:
    def __init__(self):
        self.nodes_evaluated = 0
        self.cutoffs = 0

    def solve(self, tree: Dict[str, Any], node: str, depth: int, alpha: float, beta: float, is_max: bool) -> float:
        self.nodes_evaluated += 1
        if depth == 0 or "children" not in tree[node]:
            return tree[node].get("value", 0)

        children = tree[node]["children"]
        if is_max:
            val = float('-inf')
            for child in children:
                res = self.solve(tree, child, depth - 1, alpha, beta, False)
                val = max(val, res)
                alpha = max(alpha, val)
                if beta <= alpha:
                    self.cutoffs += 1
                    break
            return val
        else:
            val = float('inf')
            for child in children:
                res = self.solve(tree, child, depth - 1, alpha, beta, True)
                val = min(val, res)
                beta = min(beta, val)
                if beta <= alpha:
                    self.cutoffs += 1
                    break
            return val

# ======================================================================================
# TASK 5: AC-3 CONSTRAINT PROPAGATION (CSP)
# ======================================================================================

def ac3_algorithm(variables: List[str], domains: Dict[str, List[int]], constraints: Dict[Tuple[str, str], Any]) -> Tuple[bool, Dict[str, List[int]], int]:
    queue = deque([arc for arc in constraints.keys()])
    domain_copy = {v: list(domains[v]) for v in variables}
    checks = 0

    def revise(xi: str, xj: str) -> bool:
        nonlocal checks
        revised = False
        to_remove = []
        for x in domain_copy[xi]:
            has_support = False
            for y in domain_copy[xj]:
                checks += 1
                if constraints[(xi, xj)](x, y):
                    has_support = True
                    break
            if not has_support:
                to_remove.append(x)
                revised = True
        for val in to_remove:
            domain_copy[xi].remove(val)
        return revised

    while queue:
        xi, xj = queue.popleft()
        if revise(xi, xj):
            if len(domain_copy[xi]) == 0:
                return False, domain_copy, checks
            for xk in variables:
                if xk != xi and xk != xj and (xk, xi) in constraints:
                    queue.append((xk, xi))

    return True, domain_copy, checks

# ======================================================================================
# TASK 6: COMBINATORIAL OPTIMIZATION (TSP EXHAUSTIVE vs 2-OPT)
# ======================================================================================

def calculate_tour_length(tour: List[int], dist_matrix: List[List[float]]) -> float:
    length = 0.0
    for i in range(len(tour)):
        length += dist_matrix[tour[i]][tour[(i + 1) % len(tour)]]
    return length

def tsp_exhaustive_search(dist_matrix: List[List[float]]) -> Tuple[List[int], float, int, float]:
    n = len(dist_matrix)
    cities = list(range(1, n))
    best_tour = None
    min_length = float('inf')
    evaluated = 0
    t0 = time.perf_counter()
    
    for perm in itertools.permutations(cities):
        evaluated += 1
        tour = [0] + list(perm)
        L = calculate_tour_length(tour, dist_matrix)
        if L < min_length:
            min_length = L
            best_tour = tour
            
    t1 = time.perf_counter()
    return best_tour, min_length, evaluated, t1 - t0

def tsp_2opt_local_search(dist_matrix: List[List[float]], max_iter: int = 1000) -> Tuple[List[int], float, int, float]:
    n = len(dist_matrix)
    tour = list(range(n))
    best_dist = calculate_tour_length(tour, dist_matrix)
    t0 = time.perf_counter()
    evaluations = 0

    improved = True
    iterations = 0
    while improved and iterations < max_iter:
        improved = False
        iterations += 1
        for i in range(1, n - 1):
            for k in range(i + 1, n):
                evaluations += 1
                new_tour = tour[:i] + tour[i:k+1][::-1] + tour[k+1:]
                new_dist = calculate_tour_length(new_tour, dist_matrix)
                if new_dist < best_dist - 1e-9:
                    best_dist = new_dist
                    tour = new_tour
                    improved = True
                    break
            if improved:
                break
                
    t1 = time.perf_counter()
    return tour, best_dist, evaluations, t1 - t0

# ======================================================================================
# TASK 7: DAY-4 REDESIGN - MINIMAX WITH ZOBRIST TRANSPOSITION TABLE CACHING
# ======================================================================================

class TranspositionMinimax:
    def __init__(self):
        self.tt: Dict[int, Tuple[int, float, str]] = {} # hash -> (depth, value, flag)
        self.nodes_evaluated = 0
        self.tt_hits = 0

    def solve(self, state_hash: int, depth: int, alpha: float, beta: float, is_max: bool,
              eval_fn: Any, get_successors: Any) -> float:
        self.nodes_evaluated += 1
        
        # Transposition Table Lookup
        if state_hash in self.tt:
            tt_depth, tt_val, tt_flag = self.tt[state_hash]
            if tt_depth >= depth:
                self.tt_hits += 1
                if tt_flag == 'EXACT':
                    return tt_val
                elif tt_flag == 'LOWERBOUND':
                    alpha = max(alpha, tt_val)
                elif tt_flag == 'UPPERBOUND':
                    beta = min(beta, tt_val)
                if alpha >= beta:
                    return tt_val

        if depth == 0:
            return eval_fn(state_hash)

        successors = get_successors(state_hash, is_max)
        if not successors:
            return eval_fn(state_hash)

        orig_alpha = alpha
        if is_max:
            best_val = float('-inf')
            for child_hash in successors:
                val = self.solve(child_hash, depth - 1, alpha, beta, False, eval_fn, get_successors)
                best_val = max(best_val, val)
                alpha = max(alpha, best_val)
                if beta <= alpha:
                    break
        else:
            best_val = float('inf')
            for child_hash in successors:
                val = self.solve(child_hash, depth - 1, alpha, beta, True, eval_fn, get_successors)
                best_val = min(best_val, val)
                beta = min(beta, best_val)
                if beta <= alpha:
                    break

        # Store entry in Transposition Table
        flag = 'EXACT'
        if best_val <= orig_alpha:
            flag = 'UPPERBOUND'
        elif best_val >= beta:
            flag = 'LOWERBOUND'
        self.tt[state_hash] = (depth, best_val, flag)
        return best_val

# ======================================================================================
# BENCHMARK RUNNER
# ======================================================================================

if __name__ == "__main__":
    print("=" * 75)
    print("CSA1714 Assignment 2: Informed Search, CSP & Adversarial Optimization")
    print("Student: Bhuvanesh H (192524027)")
    print("=" * 75)

    # Task 1 Demo: Concave Dead-End Map
    grid = [[0]*20 for _ in range(20)]
    for r in range(5, 15):
        grid[r][12] = 1
    for c in range(5, 13):
        grid[5][c] = 1
        grid[14][c] = 1

    print("\n--- Task 1: Navigation under Concave Dead-End Obstacle ---")
    for algo in ['ucs', 'greedy', 'astar']:
        res = search_grid(grid, (0, 0), (19, 19), mode=algo)
        print(f"[{res['mode']:6s}] Path Cost: {res['cost']:3d} | Nodes Expanded: {res['expanded']:4d} | Runtime: {res['runtime_sec']:.5f}s")

    # Task 5 Demo: Exam Timetabling AC-3
    print("\n--- Task 5: AC-3 Constraint Satisfaction Verification ---")
    vars_list = ['CS1', 'CS2', 'CS3', 'CS4']
    domains_data = {v: [1, 2, 3] for v in vars_list}
    constraints_data = {
        ('CS1', 'CS2'): lambda x, y: x != y,
        ('CS2', 'CS1'): lambda x, y: x != y,
        ('CS1', 'CS3'): lambda x, y: x < y,
        ('CS3', 'CS1'): lambda x, y: y < x,
        ('CS2', 'CS4'): lambda x, y: x != y,
        ('CS4', 'CS2'): lambda x, y: x != y,
    }
    solvable, reduced_doms, checks_cnt = ac3_algorithm(vars_list, domains_data, constraints_data)
    print(f"Solvable: {solvable} | Arc Consistency Checks: {checks_cnt}")
    for v in vars_list:
        print(f"  {v}: {reduced_doms[v]}")

    # Task 6 Demo: TSP Enumeration vs 2-Opt
    print("\n--- Task 6: TSP Combinatorial vs 2-Opt Benchmark ---")
    for n_pts in [6, 9]:
        random.seed(42)
        pts = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(n_pts)]
        d_mat = [[((pts[i][0]-pts[j][0])**2 + (pts[i][1]-pts[j][1])**2)**0.5 for j in range(n_pts)] for i in range(n_pts)]
        _, ex_len, ex_cnt, ex_time = tsp_exhaustive_search(d_mat)
        _, opt_len, opt_cnt, opt_time = tsp_2opt_local_search(d_mat)
        gap = (opt_len - ex_len) / ex_len * 100
        print(f"N={n_pts:2d} | Exhaustive: {ex_len:6.2f} (Time: {ex_time:.4f}s, Evals: {ex_cnt:6d}) | 2-Opt: {opt_len:6.2f} (Gap: {gap:4.2f}%, Evals: {opt_cnt:4d})")

    print("=" * 75)
