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
                                board[i][column] = "X"
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


def ship_overlaps():
    pass


def user_input():
    pass


def count_hit_ships():
    pass


def turn(board):
    pass


# while True:

