"""
Experiment 8: Depth-First Search (DFS) on Graph
Student: Bhuvanesh H (192524027)
Course: CSA1714 - Artificial Intelligence
"""

def depth_first_search(adj_graph, start_node='A'):
    visited_nodes = set()
    
    def dfs_recursive(node):
        if node not in visited_nodes:
            print(node, end=" ")
            visited_nodes.add(node)
            for neighbor in adj_graph.get(node, []):
                dfs_recursive(neighbor)
                
    dfs_recursive(start_node)
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
    depth_first_search(graph, 'A')
