# Tic-Tac-Toe Game

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check if a player has won
def check_win(board, player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player or \
           board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or \
       board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

# Function to play the game
def play_game():
    # Initialize the board
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    game_over = False

    # Main game loop
    while not game_over:
        print_board(board)

        # Get player's move
        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))

        # Check if the move is valid
        if board[row][col] == " ":
            board[row][col] = player
            if check_win(board, player):
                print_board(board)
                print("Player", player, "wins!")
                game_over = True
            elif all(board[i][j] != " " for i in range(3) for j in range(3)):
                print_board(board)
                print("It's a tie!")
                game_over = True
            else:
                player = "O" if player == "X" else "X"
        else:
            print("Invalid move. Try again.")

# Start the game
play_game()
