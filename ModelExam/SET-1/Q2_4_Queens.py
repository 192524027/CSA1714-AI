"""
========================================================================================
CSA1714 - Artificial Intelligence | Model Exam: SET 1 - Question 2
Problem: 4-Queens Problem using Backtracking Technique
Student Name: Bhuvanesh H
Register No: 192524027
Course: CSA1714 - Artificial Intelligence
========================================================================================
"""

def is_safe(board, row, col, n):
    """
    Check if a queen can be safely placed at board[row][col].
    Checks upper column, upper-left diagonal, and upper-right diagonal.
    """
    # 1. Check vertical column above
    for i in range(row):
        if board[i][col] == 'Q':
            return False
            
    # 2. Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1
        
    # 3. Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1
        
    return True

def print_board(board, n, solution_idx):
    """Utility to print the chessboard configuration."""
    print(f"\n--- Solution #{solution_idx} ---")
    positions = []
    for r in range(n):
        row_str = " ".join(board[r])
        c = board[r].index('Q')
        positions.append(f"Row {r}: Col {c}")
        print(f"  {row_str}")
    print(f"Queen Coordinates: {', '.join(positions)}")

def solve_n_queens(row, board, n, solutions):
    """
    Recursive backtracking function to find all possible placements of N-Queens.
    """
    # Base case: all N queens have been placed
    if row == n:
        solution_copy = [row_cells[:] for row_cells in board]
        solutions.append(solution_copy)
        print_board(board, n, len(solutions))
        return

    # Try placing queen in each column of current row
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 'Q'        # Place queen
            solve_n_queens(row + 1, board, n, solutions)  # Recurse
            board[row][col] = '.'        # Backtrack

def solve_4_queens():
    """Main solver for 4-Queens problem."""
    n = 4
    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []
    
    print("=" * 60)
    print("4-Queens Problem Solver using Backtracking")
    print(f"Board Size: {n}x{n} | Goal: Place {n} non-attacking Queens")
    print("=" * 60)
    
    solve_n_queens(0, board, n, solutions)
    
    print("\n" + "=" * 60)
    print(f"Search Complete: Total Solutions Found = {len(solutions)}")
    print("=" * 60)
    return solutions

if __name__ == "__main__":
    solve_4_queens()
