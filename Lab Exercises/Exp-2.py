"""
Experiment 2: 8-Queens Problem using Backtracking
Student: Bhuvanesh H (192524027)
Course: CSA1714 - Artificial Intelligence
"""

N = 8

def is_safe(board, row, col):
    # Check if a queen placed in previous rows conflicts with (row, col)
    for prev_row in range(row):
        prev_col = board[prev_row]
        # Same column or diagonal conflict
        if prev_col == col or abs(prev_col - col) == abs(prev_row - row):
            return False
    return True

def solve_queens(board, current_row):
    if current_row == N:
        return True
    
    for col in range(N):
        if is_safe(board, current_row, col):
            board[current_row] = col
            if solve_queens(board, current_row + 1):
                return True
            board[current_row] = -1  # Backtrack
            
    return False

if __name__ == "__main__":
    queen_positions = [-1] * N
    if solve_queens(queen_positions, 0):
        print(queen_positions)
    else:
        print("No solution found")
