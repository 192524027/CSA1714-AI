"""
Experiment 10: A* Search Algorithm
Student: Bhuvanesh H (192524027)
Course: CSA1714 - Artificial Intelligence
"""

import heapq

def a_star_search(graph, heuristics, start, goal):
    # Priority Queue stores: (f_score, g_score, current_node, path)
    priority_queue = [(heuristics[start], 0, start, [start])]
    visited = set()
    
    while priority_queue:
        f_score, g_cost, node, path = heapq.heappop(priority_queue)
        
        if node == goal:
            print("Path:", path)
            print("Cost:", g_cost)
            return
            
        if node in visited:
            continue
        visited.add(node)
        
        for neighbor, edge_weight in graph.get(node, {}).items():
            if neighbor not in visited:
                tentative_g = g_cost + edge_weight
                total_f = tentative_g + heuristics.get(neighbor, 0)
                heapq.heappush(priority_queue, (total_f, tentative_g, neighbor, path + [neighbor]))
                
    print("Path not found")

if __name__ == "__main__":
    graph_network = {
        'A': {'B': 1, 'C': 4},
        'B': {'D': 2, 'E': 5},
        'C': {'E': 1},
        'D': {'G': 5},
        'E': {'G': 3},
        'G': {}
    }
    
    heuristic_values = {
        'A': 7,
        'B': 6,
        'C': 4,
        'D': 4,
        'E': 2,
        'G': 0
    }
    
    a_star_search(graph_network, heuristic_values, 'A', 'G')
