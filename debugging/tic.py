#!/usr/bin/python3

def print_board(board):
for row in board:
print(" | ".join(row))
print("-" * 5)

def check_winner(board):
# Rows
for row in board:
if row[0] != " " and row.count(row[0]) == 3:
return row[0]

# Columns
for col in range(3):
if board[0][col] != " " and board[0][col] == board[1][col] == board[2][col]:
return board[0][col]

# Diagonals
if board[0][0] != " " and board[0][0] == board[1][1] == board[2][2]:
return board[0][0]

if board[0][2] != " " and board[0][2] == board[1][1] == board[2][0]:
return board[0][2]

return None

def tic_tac_toe():
board = [[" "]*3 for _ in range(3)]
player = "X"

while True:
print_board(board)

try:
row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
except ValueError:
print("Please enter numbers only.\n")
continue

# Validate range
if row not in [0, 1, 2] or col not in [0, 1, 2]:
print("Invalid position. Must be 0, 1, or 2.\n")
continue

# Check if spot is free
if board[row][col] != " ":
print("That spot is already taken! Try again.\n")
continue

# Place the mark
board[row][col] = player

# Check winner
winner = check_winner(board)
if winner:
print_board(board)
print(f"Player {winner} wins!")
break

# Switch players
player = "O" if player == "X" else "X"

# Optional: Detect tie
if all(all(cell != " " for cell in row) for row in board):
print_board(board)
print("It's a tie!")
break


tic_tac_toe()

