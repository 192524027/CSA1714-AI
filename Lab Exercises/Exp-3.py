"""
Experiment 3: Water Jug Problem using BFS
Student: Bhuvanesh H (192524027)
Course: CSA1714 - Artificial Intelligence
"""

from collections import deque

def solve_water_jug(cap_a=4, cap_b=3, goal=2):
    start_state = (0, 0)
    queue = deque([(start_state, [])])
    visited = {start_state}
    
    while queue:
        (curr_a, curr_b), path = queue.popleft()
        
        if curr_a == goal or curr_b == goal:
            print("Solution:")
            for step in path:
                print(step)
            print((curr_a, curr_b))
            return
        
        # Possible successor transitions
        transitions = [
            ((cap_a, curr_b), "Fill A"),
            ((curr_a, cap_b), "Fill B"),
            ((0, curr_b), "Empty A"),
            ((curr_a, 0), "Empty B"),
            # Pour A -> B
            ((curr_a - min(curr_a, cap_b - curr_b), curr_b + min(curr_a, cap_b - curr_b)), "A -> B"),
            # Pour B -> A
            ((curr_a + min(curr_b, cap_a - curr_a), curr_b - min(curr_b, cap_a - curr_a)), "B -> A")
        ]
        
        for next_state, action in transitions:
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [action]))

if __name__ == "__main__":
    solve_water_jug(4, 3, 2)
