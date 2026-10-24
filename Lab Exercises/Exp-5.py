"""
Experiment 5: Missionaries and Cannibals Problem
Student: Bhuvanesh H (192524027)
Course: CSA1714 - Artificial Intelligence
"""

from collections import deque

def is_valid_state(missionaries, cannibals):
    # Check bounds
    if not (0 <= missionaries <= 3 and 0 <= cannibals <= 3):
        return False
    # Check if cannibals outnumber missionaries on either bank
    if missionaries > 0 and cannibals > missionaries:
        return False
    right_m = 3 - missionaries
    right_c = 3 - cannibals
    if right_m > 0 and right_c > right_m:
        return False
    return True

def solve_missionaries_cannibals():
    # State format: (missionaries_left, cannibals_left, boat_pos)
    # boat_pos: 0 for left bank, 1 for right bank
    initial_state = (3, 3, 0)
    goal_state = (0, 0, 1)
    
    # Possible boat loads: (m, c)
    boat_moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
    
    frontier = deque([(initial_state, [])])
    visited = {initial_state}
    
    while frontier:
        current, path = frontier.popleft()
        m, c, boat = current
        
        if current == goal_state:
            print("Solution:")
            for state in path + [current]:
                print(state)
            return
            
        for dm, dc in boat_moves:
            if boat == 0:
                next_state = (m - dm, c - dc, 1)
            else:
                next_state = (m + dm, c + dc, 0)
                
            if is_valid_state(next_state[0], next_state[1]) and next_state not in visited:
                visited.add(next_state)
                frontier.append((next_state, path + [current]))

if __name__ == "__main__":
    solve_missionaries_cannibals()
