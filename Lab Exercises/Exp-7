"""
Experiment 7: Breadth-First Search (BFS) on Graph
Student: Bhuvanesh H (192524027)
Course: CSA1714 - Artificial Intelligence
"""

from collections import deque

def breadth_first_search(adj_graph, start_node='A'):
    visited_nodes = set()
    queue = deque([start_node])
    
    while queue:
        current_node = queue.popleft()
        
        if current_node not in visited_nodes:
            print(current_node, end=" ")
            visited_nodes.add(current_node)
            queue.extend(adj_graph.get(current_node, []))
    print()

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': [],
        'F': []
    }
    breadth_first_search(graph, 'A')
