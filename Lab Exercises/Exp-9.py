"""
Experiment 9: Traveling Salesperson Problem (Greedy Nearest Neighbor)
Student: Bhuvanesh H (192524027)
Course: CSA1714 - Artificial Intelligence
"""

def tsp_nearest_neighbor(distance_matrix, origin_city=0):
    num_cities = len(distance_matrix)
    visited_cities = {origin_city}
    tour_route = [origin_city]
    accumulated_cost = 0
    active_city = origin_city
    
    while len(visited_cities) < num_cities:
        # Select unvisited city with lowest transition cost
        closest_city = min(
            (c for c in range(num_cities) if c not in visited_cities),
            key=lambda c: distance_matrix[active_city][c]
        )
        accumulated_cost += distance_matrix[active_city][closest_city]
        tour_route.append(closest_city)
        visited_cities.add(closest_city)
        active_city = closest_city
        
    # Complete cycle by returning to origin
    accumulated_cost += distance_matrix[active_city][origin_city]
    tour_route.append(origin_city)
    
    print("Path:", " -> ".join(map(str, tour_route)))
    print("Total Cost:", accumulated_cost)

if __name__ == "__main__":
    distance_graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    tsp_nearest_neighbor(distance_graph, 0)
