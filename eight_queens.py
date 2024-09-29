import tkinter as tk

class Chessboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("8 Queens Problem")
        self.geometry("400x400")
        self.resizable(False, False)

        # Create a canvas to draw the chessboard
        self.canvas = tk.Canvas(self, width=400, height=400)
        self.canvas.pack()

        # Initialize the board
        self.board = [[0 for _ in range(8)] for _ in range(8)]

        # Draw the initial chessboard
        self.draw_board()

        # Solve the 8 queens problem and display the solution
        self.solve()

    def draw_board(self):
        """Draw an 8x8 chessboard with alternating black and white squares."""
        square_size = 50
        for row in range(8):
            for col in range(8):
                color = "white" if (row + col) % 2 == 0 else "black"
                self.canvas.create_rectangle(
                    col * square_size,
                    row * square_size,
                    (col + 1) * square_size,
                    (row + 1) * square_size,
                    fill=color
                )

    def place_queen(self, row, col):
        """Place a queen (represented as a red circle) on the board."""
        square_size = 50
        x_center = col * square_size + square_size // 2
        y_center = row * square_size + square_size // 2
        radius = square_size // 3
        self.canvas.create_oval(
            x_center - radius,
            y_center - radius,
            x_center + radius,
            y_center + radius,
            fill="red"
        )

    def is_safe(self, row, col):
        """Check if placing a queen at (row, col) is safe."""
        # Check the current column
        for i in range(row):
            if self.board[i][col] == 1:
                return False

        # Check upper left diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        # Check upper right diagonal
        for i, j in zip(range(row, -1, -1), range(col, 8)):
            if self.board[i][j] == 1:
                return False

        return True

    def solve_nqueens(self, row):
        """Solve the 8 queens problem using backtracking."""
        if row == 8:
            return True

        for col in range(8):
            if self.is_safe(row, col):
                self.board[row][col] = 1
                if self.solve_nqueens(row + 1):
                    self.place_queen(row, col)
                    return True
                self.board[row][col] = 0

        return False

    def solve(self):
        """Start solving the 8 queens problem from the first row."""
        self.solve_nqueens(0)

# Create and run the application
if __name__ == "__main__":
    app = Chessboard()
    app.mainloop()
