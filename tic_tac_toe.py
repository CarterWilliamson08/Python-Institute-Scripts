import random
import time

# Initialize variables
game = False
board = {
    1: 0, 2: 0, 3: 0,
    4: 0, 5: 0, 6: 0,
    7: 0, 8: 0, 9: 0
    }

# The function displays the board.
def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print("+-------+-------+-------+")
    for i in range(0, 9, 3):
        print("|       |       |       |")
        print("|   " + str(check_num(i+1, board)) + "   |   " + str(check_num(i+2, board)) + "   |   " + str(check_num(i+3, board)) + "   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")

# The function makes a list of all free fields to choose from.
def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = []
    for fields in board:
        if board[fields] == 0:
            free_fields.append(fields)

    return free_fields

# Checks for victory conditions, ends the game if victory is achieved.
def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    wins = [(1,2,3),
            (4,5,6),
            (7,8,9),
            (1,4,7),
            (2,5,8),
            (3,6,9),
            (1,5,9),
            (3,5,7)]

    for a, b, c in wins:
        if board[a] == sign and board[b] == sign and board[c] == sign:
            return True

    return False

# The function allows the player to choose a spot on the board and updates it.
def enter_move(board):
    global game
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.

    free_fields = make_list_of_free_fields(board)
    try:
        player_input = int(input("Enter your move: "))

        if player_input in free_fields:
            # IMPORTANT FIX:
            # free_fields is a list like [1, 3, 4, 9]
            # so you should use player_input directly, not free_fields[player_input]
            print(f"Player chose: {player_input}")
            board[player_input] = 1

            display_board(board)

            if victory_for(board, 1) is True:
                print("Player wins!")
                game = True
                return  # stop the recursion chain

            # Draw check: if no free spots left after player's move
            if len(make_list_of_free_fields(board)) == 0:
                print("It's a draw!")
                game = True
                return

            draw_move(board)
        else:
            print("Spot is taken!")
            enter_move(board)

    except ValueError:
        print("Please enter a valid number.")
        enter_move(board)

# The function draws the computer's move and updates the board.
def draw_move(board):
    global game
    time.sleep(1)
    free_fields = make_list_of_free_fields(board)

    # If no moves left, it's a draw (prevents random errors too)
    if len(free_fields) == 0:
        print("It's a draw!")
        game = True
        return

    # IMPORTANT FIX:
    # randint(1, len(free_fields)) can go out of range and skips index 0.
    # Instead, choose a free spot directly.
    com_input = random.choice(free_fields)

    print(f"Computer chose: {com_input}")
    board[com_input] = 2

    display_board(board)

    if victory_for(board, 2) is True:
        game = True
        return  # stop the recursion chain

    enter_move(board)

# Checks if a position on the board is an "X" or an "O"
def check_num(pos, board):
    if board[pos] == 0:
        return pos
    elif board[pos] == 1:
        return "X"
    else:
        return "O"


# Main function
coinflip = random.randint(0, 1)
print("Coinflip to see who goes first...")
time.sleep(1)

while game is False:
    first = None
    if coinflip == 0:
        first = "Player"
        print(f"Computer showed {coinflip}, so {first} goes first!")
        time.sleep(2)
        coinflip = 5
        display_board(board)
        enter_move(board)
    elif coinflip == 1:
        first = "Computer"
        print(f"Computer showed {coinflip}, so {first} goes first!")
        time.sleep(2)
        coinflip = 5
        display_board(board)
        draw_move(board)
    else:
        continue