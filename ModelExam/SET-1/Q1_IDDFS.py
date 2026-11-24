"""
========================================================================================
CSA1714 - Artificial Intelligence | Model Exam: SET 1 - Question 1
Problem: Iterative Deepening Depth First Search (IDDFS) on State-Space Graph
Student Name: Bhuvanesh H
Register No: 192524027
Course: CSA1714 - Artificial Intelligence
========================================================================================
"""

def depth_limited_search(graph, current, goal, limit, path):
    """
    Performs Depth-Limited Search (DLS) up to the specified depth limit.
    Returns the path if goal is found, None if cutoff occurs without finding goal.
    """
    path.append(current)
    
    # Check if goal reached
    if current == goal:
        return path
    
    # If limit reached, backtrack
    if limit <= 0:
        path.pop()
        return None
    
    # Explore neighbors recursively
    for neighbor in graph.get(current, []):
        if neighbor not in path:  # Cycle prevention
            result = depth_limited_search(graph, neighbor, goal, limit - 1, path)
            if result is not None:
                return result
                
    path.pop()  # Backtrack
    return None

def iddfs(graph, start, goal, max_depth=10):
    """
    Performs Iterative Deepening Depth First Search (IDDFS).
    Gradually increases the depth limit until the goal is found or max_depth is reached.
    """
    print("=" * 65)
    print("Iterative Deepening Depth First Search (IDDFS)")
    print(f"Start Node: '{start}' | Goal Node: '{goal}'")
    print("=" * 65)
    
    for depth in range(max_depth + 1):
        print(f"Searching at Depth Limit = {depth}...")
        path = []
        result = depth_limited_search(graph, start, goal, depth, path)
        if result is not None:
            print(f"\n>> Goal '{goal}' Found at Depth {depth}!")
            print(f">> Solution Path: {' -> '.join(result)}")
            print(f">> Total Steps (Path Length): {len(result) - 1}")
            return result
            
    print(f"\n>> Goal '{goal}' not found within maximum depth {max_depth}.")
    return None

if __name__ == "__main__":
    # State-Space Graph representation
    #         A
    #       /   \
    #      B     C
    #     / \   / \
    #    D   E F   G
    #   /   /
    #  H   J
    state_space_graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F', 'G'],
        'D': ['H'],
        'E': ['J'],
        'F': [],
        'G': [],
        'H': [],
        'J': []
    }
    
    start_node = 'A'
    goal_node = 'J'
    
    solution = iddfs(state_space_graph, start_node, goal_node, max_depth=5)
