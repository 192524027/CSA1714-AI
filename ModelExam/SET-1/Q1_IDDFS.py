# Iterative Deepening Depth First Search (IDDFS)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

def dls(node, goal, depth, path):
    path.append(node)
    if node == goal:
        return path
    if depth <= 0:
        path.pop()
        return None
    for neighbor in graph.get(node, []):
        result = dls(neighbor, goal, depth - 1, path)
        if result:
            return result
    path.pop()
    return None

def iddfs(start, goal, max_depth):
    for depth in range(max_depth):
        path = []
        result = dls(start, goal, depth, path)
        if result:
            return result
    return None

start = 'A'
goal = 'E'
path = iddfs(start, goal, 5)

if path:
    print("Path from initial to goal node:")
    print(" -> ".join(path))
else:
    print("Path not found")
