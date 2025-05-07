# Function to initialize the game board
def initialize_board():
    return [' ' for _ in range(9)]  # List of 9 empty spaces representing the board

# Function to print the current state of the game board
def print_board(board):
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")

# Function to check if the game has been won
def check_win(board, player):
    # All possible winning combinations
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # vertical
        [0, 4, 8], [2, 4, 6]              # diagonal
    ]
    
    # Check each winning condition
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Function to check if the game is a draw
def check_draw(board):
    return all(cell != ' ' for cell in board)

# Function to take a player's move
def player_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Invalid input. Please enter a number between 1 and 9.")
            elif board[move] != ' ':
                print("That spot is already taken. Try again.")
            else:
                board[move] = player
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

# Main function to control the game
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print("Player 1: X | Player 2: O\n")
    
    board = initialize_board()
    current_player = 'X'
    
    while True:
        print_board(board)
        
        # Player makes a move
        player_move(board, current_player)
        
        # Check if the current player has won
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        # Check if the game is a draw
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch player for the next turn
        current_player = 'O' if current_player == 'X' else 'X'
    
# Run the game
if __name__ == "__main__":
    play_game()
