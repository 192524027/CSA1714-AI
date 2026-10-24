"""
Experiment 1: 8-Puzzle Problem using Breadth-First Search (BFS)
Student: Bhuvanesh H (192524027)
Course: CSA1714 - Artificial Intelligence
"""

from collections import deque

def solve_8_puzzle(start_state, goal_state):
    # Queue stores: (current_board_tuple, path_of_moves)
    frontier = deque([(start_state, [])])
    visited = {start_state}
    
    # Legal sliding moves for the blank space (0)
    move_offsets = [
        ("Up", -1, 0),
        ("Down", 1, 0),
        ("Left", 0, -1),
        ("Right", 0, 1)
    ]
    
    while frontier:
        state, path = frontier.popleft()
        
        if state == goal_state:
            return path
        
        blank_idx = state.index(0)
        row, col = divmod(blank_idx, 3)
        
        for move_name, d_row, d_col in move_offsets:
            new_row, new_col = row + d_row, col + d_col
            
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_blank_idx = new_row * 3 + new_col
                next_state = list(state)
                next_state[blank_idx], next_state[new_blank_idx] = next_state[new_blank_idx], next_state[blank_idx]
                next_state_tuple = tuple(next_state)
                
                if next_state_tuple not in visited:
                    visited.add(next_state_tuple)
                    frontier.append((next_state_tuple, path + [move_name]))
    return None

if __name__ == "__main__":
    initial_board = (1, 2, 3, 4, 0, 6, 7, 5, 8)
    target_board = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    
    solution_path = solve_8_puzzle(initial_board, target_board)
    print("Solution:", solution_path)
