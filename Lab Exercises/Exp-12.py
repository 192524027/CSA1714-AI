"""
Experiment 12: Tic-Tac-Toe Game
Student: Bhuvanesh H (192524027)
Course: CSA1714 - Artificial Intelligence
"""

class TicTacToe:
    def __init__(self):
        self.grid = [' '] * 9

    def render_board(self):
        print()
        for row in range(0, 9, 3):
            print(f" {self.grid[row]} | {self.grid[row+1]} | {self.grid[row+2]} ")
            if row < 6:
                print("---+---+---")

    def check_winner(self, player):
        winning_triplets = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)              # Diagonals
        ]
        return any(all(self.grid[pos] == player for pos in combo) for combo in winning_triplets)

    def is_full(self):
        return ' ' not in self.grid

    def play(self, simulated_moves=None):
        current_turn = 'X'
        move_index = 0
        
        while True:
            self.render_board()
            
            if simulated_moves and move_index < len(simulated_moves):
                raw_input = simulated_moves[move_index]
                move_index += 1
                print(f"Player {current_turn}, enter position (1-9): {raw_input}")
            else:
                try:
                    raw_input = input(f"Player {current_turn}, enter position (1-9): ")
                except EOFError:
                    break
                    
            try:
                pos = int(raw_input) - 1
            except ValueError:
                print("Enter a valid number.")
                continue

            if pos < 0 or pos > 8 or self.grid[pos] != ' ':
                print("Invalid move! Try again.")
                continue

            self.grid[pos] = current_turn

            if self.check_winner(current_turn):
                self.render_board()
                print("Player", current_turn, "wins!")
                return

            if self.is_full():
                self.render_board()
                print("It's a draw!")
                return

            current_turn = 'O' if current_turn == 'X' else 'X'

if __name__ == "__main__":
    game = TicTacToe()
    game.play()
