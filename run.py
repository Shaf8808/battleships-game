import random

LENGTH_OF_SHIPS = [2, 3, 4, 5, 6]
PLAYER_BOARD = [[" "] * 8 for x in range(8)]
COMPUTER_BOARD = [[" "] * 8 for x in range(8)]
PLAYER_GUESS_BOARD = [[" "] * 8 for x in range(8)]
COMPUTER_GUESS_BOARD = [[" "] * 8 for x in range(8)]
LETTERS_TO_NUMBERS = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7
}


def print_board(board):
    """
    The structure and layout of the board
    which is presented to the user once they
    begin the game
    """
    print("  A B C D E F G H")
    print("  +-+-+-+-+-+-+-+")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


def place_ships(board):
    # loop through length of ships
    for ship_length in LENGTH_OF_SHIPS:
        # loop until ship fits and doesn't overlap
        while True:
            if board == COMPUTER_BOARD:
                orientation = random.choice(["H", "V"])
                row, column = random.randint(0, 7), random.randint(0, 7)
                if check_ship_fits(ship_length, row, column, orientation):
                    # checks to see if ship overlaps
                    if ship_overlaps(board, row, column, orientation, ship_length) == False:
                        # if not, the ship is placed
                        if orientation == "H":
                            for x in range(column, column + ship_length):
                                board[row][x] = "X"
                        else:
                            for x in range(row, row + ship_length):
                                board[x][column] = "X"
                        break
            else:
                place_ship = True
                print('Place the ship with a length of ' + str(ship_length))
                row, column, orientation = user_input(place_ship)
                if check_ship_fits(ship_length, row, column, orientation):
                    #check if ship overlaps
                        if ship_overlaps(board, row, column, orientation, ship_length) == False:
                            #place ship
                            if orientation == "H":
                                for i in range(column, column + ship_length):
                                    board[row][i] = "X"
                            else:
                                for i in range(row, row + ship_length):
                                    board[i][column] = "X"
                            print_board(PLAYER_BOARD)
                            break 


def check_ship_fits(ship_length, row, column, orientation):
    if orientation == "H":
        if column + ship_length > 8:
            return False
        else:
            return True
    else:
        if row + ship_length > 8:
            return False
        else:
            return True


def ship_overlaps(board, row, column, orientation, ship_length):
    if orientation == "H":
        for x in range(column, column + ship_length):
            if board[row][x] == "X":
                return True
    else:
        for x in range(row, row + ship_length):
            if board[x][column] == "X":
                return True
    return False


def user_input(place_ship):
    if place_ship == True:
        while True:
            try: 
                orientation = input("Enter orientation (H or V): ").upper()
                if orientation == "H" or orientation == "V":
                    break
            except TypeError:
                print('Enter a valid orientation H or V')
        while True:
            try: 
                row = input("Enter the row 1-8 of the ship: ")
                if row in '12345678':
                    row = int(row) - 1
                    break
            except ValueError:
                print('Enter a valid number between 1-8')
        while True:
            try: 
                column = input("Enter the column of the ship: ").upper()
                if column in 'ABCDEFGH':
                    column = LETTERS_TO_NUMBERS[column]
                    break
            except KeyError:
                print('Enter a valid letter between A-H')
        return row, column, orientation 
    else:
        while True:
            try: 
                row = input("Enter the row 1-8 of the ship: ")
                if row in '12345678':
                    row = int(row) - 1
                    break
            except ValueError:
                print('Enter a valid number between 1-8')
        while True:
            try: 
                column = input("Enter the column of the ship: ").upper()
                if column in 'ABCDEFGH':
                    column = LETTERS_TO_NUMBERS[column]
                    break
            except KeyError:
                print('Enter a valid letter between A-H')
        return row, column        


def count_hit_ships(board):
    """
    Increments number of hit ships if
    guess is correct
    """
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count 


def turn(board):
    """
    Function for both the user's turn as well as the computer's
    turn. Informs user and computer if they have selected the same
    position as a previous turn
    """
    if board == PLAYER_GUESS_BOARD:
        row, column = user_input(PLAYER_GUESS_BOARD)
        if board[row][column] == "-":
            turn(board)
        elif board[row][column] == "X":
            turn(board)
        elif COMPUTER_BOARD[row][column] == "X":
            board[row][column] = "X"
        else:
            board[row][column] = "-"
    else:
        row, column = random.randint(0,7), random.randint(0,7)
        if board[row][column] == "-":
            turn(board)
        elif board[row][column] == "X":
            turn(board)
        elif PLAYER_BOARD[row][column] == "X":
            board[row][column] = "X"
        else:
            board[row][column] = "-"


place_ships(COMPUTER_BOARD)
print_board(COMPUTER_BOARD)
print_board(PLAYER_BOARD)
place_ships(PLAYER_BOARD)

while True:
     # Loop for player's turn that continuously
     # runs until the user wins
    while True:
        print('Guess a battleship location')
        print_board(PLAYER_GUESS_BOARD)
        turn(PLAYER_GUESS_BOARD)
        break
    if count_hit_ships(PLAYER_GUESS_BOARD) == 17:
        print("You win!")
        break   
    # Computer's turn
    while True:
        turn(COMPUTER_GUESS_BOARD)
        break           
    print_board(COMPUTER_GUESS_BOARD)   
    if count_hit_ships(COMPUTER_GUESS_BOARD) == 17:
        print("Sorry, the computer won.")
        break


