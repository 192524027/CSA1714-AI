"""
Experiment 11: Map Coloring Problem (CSP)
Student: Bhuvanesh H (192524027)
Course: CSA1714 - Artificial Intelligence
"""

def solve_map_coloring(adj_graph, available_colors):
    region_names = list(adj_graph.keys())
    color_assignments = {}

    def is_color_valid(region, color_choice):
        # Ensure no adjacent region shares the same color
        for neighbor in adj_graph.get(region, []):
            if color_assignments.get(neighbor) == color_choice:
                return False
        return True

    def backtrack_assignment(index):
        if index == len(region_names):
            return True
            
        current_region = region_names[index]
        for color in available_colors:
            if is_color_valid(current_region, color):
                color_assignments[current_region] = color
                if backtrack_assignment(index + 1):
                    return True
                del color_assignments[current_region]  # Backtrack
                
        return False

    if backtrack_assignment(0):
        for reg, col in color_assignments.items():
            print(f"{reg} : {col}")
    else:
        print("No solution")

if __name__ == "__main__":
    territory_map = {
        'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'D'],
        'D': ['B', 'C']
    }
    palette = ['Red', 'Green', 'Blue']
    solve_map_coloring(territory_map, palette)
