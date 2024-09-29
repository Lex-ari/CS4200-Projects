import tkinter as tk

class Chessboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("8 Queens Problem - Step by Step")
        self.geometry("400x450")  # Adjusted size to accommodate button
        self.resizable(False, False)

        # Create a canvas to draw the chessboard
        self.canvas = tk.Canvas(self, width=400, height=400)
        self.canvas.pack()

        # Button to place queens one by one
        self.button = tk.Button(self, text="Place Next Queen", command=self.place_next_queen)
        self.button.pack(pady=10)

        # Initialize the board and variables for backtracking
        self.board = [[0 for _ in range(8)] for _ in range(8)]
        self.current_row = 0
        self.solution_found = False
        self.queens_positions = []  # Keep track of queens' positions
        self.column_attempts = [-1] * 8  # To track the next column to try for each row

        # Draw the initial chessboard
        self.draw_board()

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
                    fill=color,
                    tags=f"square_{row}_{col}"
                )

    def highlight_row(self, row):
        """Highlight the current row by changing its color."""
        square_size = 50
        for col in range(8):
            # Set the highlight color
            color = "#FFFF00" if (row + col) % 2 == 0 else "#FFD700"
            self.canvas.itemconfig(f"square_{row}_{col}", fill=color)
        
        # Reset other rows' colors
        for other_row in range(8):
            if other_row != row:
                for col in range(8):
                    color = "white" if (other_row + col) % 2 == 0 else "black"
                    self.canvas.itemconfig(f"square_{other_row}_{col}", fill=color)

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
            fill="red",
            tags=f"queen_{row}_{col}"
        )

    def remove_queen(self, row, col):
        """Remove a queen from the board."""
        self.canvas.delete(f"queen_{row}_{col}")

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

    def place_next_queen(self):
        """Place queens one by one with backtracking, and highlight the current row."""
        if self.solution_found:
            return  # If solution is already found, no need to place more queens

        # Highlight the current row where we're trying to place a queen
        self.highlight_row(self.current_row)

        # Handle the logic for searching for a placement
        self.search_next_move()

    def search_next_move(self):
        """Handle queen placement and backtracking with visualization of steps."""
        if self.solution_found:
            return

        # Try the next column in the current row
        self.column_attempts[self.current_row] += 1
        col = self.column_attempts[self.current_row]

        # If we've tried all columns in the current row, we need to backtrack
        if col >= 8:
            self.column_attempts[self.current_row] = -1  # Reset column attempts for this row
            if self.queens_positions:
                last_row, last_col = self.queens_positions.pop()
                self.remove_queen(last_row, last_col)
                self.board[last_row][last_col] = 0
                self.current_row = last_row  # Backtrack to the previous row
            return  # Stop for now and wait for the next button press

        # Check if placing a queen at (current_row, col) is safe
        if self.is_safe(self.current_row, col):
            # Place the queen
            self.board[self.current_row][col] = 1
            self.place_queen(self.current_row, col)
            self.queens_positions.append((self.current_row, col))

            # Move to the next row
            self.current_row += 1

            if self.current_row == 8:
                self.solution_found = True  # All queens placed successfully
                return  # Successfully placed all queens
        # If not safe, the function will try the next column on the next button press

# Create and run the application
if __name__ == "__main__":
    app = Chessboard()
    app.mainloop()
