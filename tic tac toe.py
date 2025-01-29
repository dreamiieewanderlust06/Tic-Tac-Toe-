import tkinter as tk
from tkinter import messagebox

# Function to handle button click
def on_button_click(r, c):
    global current_player

    if board[r][c] == 0:  # If the cell is empty
        board[r][c] = current_player
        buttons[r][c].config(text=current_player, bg=player_colors[current_player], fg="white")

        if check_winner(current_player):
            messagebox.showinfo("Winner!", f"Player {current_player} wins!")
            reset_board()
        elif all(board[i][j] != 0 for i in range(3) for j in range(3)):  # Check for a draw
            messagebox.showinfo("Draw", "It's a draw!")
            reset_board()

        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

# Function to check for a winner
def check_winner(player):
    for r in range(3):
        if all(board[r][c] == player for c in range(3)):  # Check rows
            return True
    for c in range(3):
        if all(board[r][c] == player for r in range(3)):  # Check columns
            return True
    if all(board[i][i] == player for i in range(3)):  # Check diagonal
        return True
    if all(board[i][2 - i] == player for i in range(3)):  # Check anti-diagonal
        return True
    return False

# Function to reset the board
def reset_board():
    global board, current_player
    board = [[0, 0, 0] for _ in range(3)]
    for r in range(3):
        for c in range(3):
            buttons[r][c].config(text="", bg="#f0f0f0", fg="black")
    current_player = 'X'

# Set up the main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Set background color and styling
root.config(bg="#2E8B57")
root.geometry("400x450")
root.resizable(False, False)

# Initialize the game variables
current_player = 'X'
board = [[0, 0, 0] for _ in range(3)]

# Define player colors
player_colors = {
    'X': "#FF6347",  # Tomato Red
    'O': "#4682B4",  # Steel Blue
}

# Create buttons for the board
buttons = [[None for _ in range(3)] for _ in range(3)]
for r in range(3):
    for c in range(3):
        buttons[r][c] = tk.Button(root, text="", font=("Arial", 30, "bold"), width=10, height=3, 
                                  command=lambda r=r, c=c: on_button_click(r, c), 
                                  relief="raised", bd=5, bg="#f0f0f0", fg="black")
        buttons[r][c].grid(row=r, column=c, padx=5, pady=5, sticky="nsew")

# Make the grid cells expand equally
for r in range(3):
    root.grid_rowconfigure(r, weight=1, uniform="equal")
for c in range(3):
    root.grid_columnconfigure(c, weight=1, uniform="equal")

# Run the application
root.mainloop()
