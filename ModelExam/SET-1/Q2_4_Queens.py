# 4-Queens Problem using Backtracking

N = 4

def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def print_board(board):
    for r in range(N):
        row = ['.'] * N
        row[board[r]] = 'Q'
        print(' '.join(row))
    print()

def solve_queens(row, board, solutions):
    if row == N:
        solutions.append(board[:])
        print_board(board)
        return
    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            solve_queens(row + 1, board, solutions)

board = [-1] * N
solutions = []
print("Solutions for 4-Queens Problem:\n")
solve_queens(0, board, solutions)
print("Total solutions found:", len(solutions))
