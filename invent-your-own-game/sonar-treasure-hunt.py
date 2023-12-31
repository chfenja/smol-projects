import random
import sys
import math

def get_new_board():
    """Create a new 60x15 board data structure."""
    board = []
    for x in range(60):
        board.append([])
        for y in range(15):
            if random.randint(0, 1) == 0:
                board[x].append("~")
            else:
                board[x].append("`")
    return board

def draw_board(board):
    """Draw the board data structure."""
    tens_digits_line = "    "
    for i in range(1, 6):
        tens_digits_line += (" " * 9) + str(i)

    print(tens_digits_line)
    print("    " + ("0123456789" * 6))
    print()

    for row in range(15):
        if row < 10:
            extra_space = " "
        else:
            extra_space = ""

        board_row = ""
        for column in range(60):
            board_row+= board[column][row]

        print(extra_space, row, board_row, row)

    print()
    print("    " + ("0123456789" * 6))
    print(tens_digits_line)

def get_random_chests(num_chests):
    """Create a list of chest data structures (two-item lists of x, y int coordinates)."""
    chests = []
    while len(chests) < num_chests:
        new_chest = [random.randint(0, 59), random.randint(0, 14)]
        if new_chest not in chests:
            chests.append(new_chest)
    return chests

def is_on_board(x, y):
    """Return True if the coordinate are on the board; otherwise, return False."""
    return x >= 0 and x <= 59 and y >= 0 and y <= 14

def make_move(board, chests, x, y):
    """
    Change the board data structure with a sonar device character.
    Remove treasure chests from the chests list as they are found.
    Return False if this is an invalid move.
    Otherwise, return the string of the result of this move.
    """
    smallest_distance = 100
    for cx, cy in chests:
        distance = math.sqrt((cx - x) * (cx - x) + (cy - y) * (cy - y))

        if distance < smallest_distance:
            smallest_distance = distance

    smallest_distance = round(smallest_distance)

    if smallest_distance == 0:
        chests.remove([x, y])
        return "You have found a sunken treasure chest!"
    else:
        if smallest_distance < 10:
            board[x][y] = str(smallest_distance)
            return f"Treasure detected at a distance of {smallest_distance} from the sonar device"
        else:
            board[x][y] = "X"
            return "Sonar did not detect anything. All treasure chests out of range"

def enter_player_move(previous_moves):
    """Let the player enter their move. Return a two-item list of int xy coordinates."""
    print("Where do you want to drop the next sonar deice? (0-59 0-14) (or type quit)")
    while True:
        move = input()
        if move.lower() == "quit":
            print("Thanks for playing!")
            sys.exit()

        move = move.split()
        if len(move) == 2 and move[0].isdigit() and move[1].isdigit and is_on_board(int(move[0]), int(move[1])):
            if [int(move[0]), int(move[1])] in previous_moves:
                print("You have already moved there.")
                continue
            return [int(move[0]), int(move[1])]

        print("Enter a number from 0 to 59, a space, then a number from 0 to 14.")

def show_instructions():
    print("""Instructions:
    You are the captain of the Simon, a treasure-hunting ship. Your current
    mission is to use sonar devices to find three sunken treasure chests at
    the bottom of the ocean. But you only have cheap sonar that finds distance,
    not direction.
    Enter the coordinates to drop a sonar device. The ocean map will be marked
    with how far away the nearest chest is, or an X if it is beyond the sonar
    device's range. For example, the C marks are where chests are. The sonar
    device shows a 3 because the closest chest is 3 spaces away.

                     1         2         3
           012345678901234567890123456789012

         0 ~~~~`~```~`~``~~~``~`~~``~~~``~`~ 0
         1 ~`~`~``~~`~```~~~```~~`~`~~~`~~~~ 1
         2 `~`C``3`~~~~`C`~~~~`````~~``~~~`` 2
         3 ````````~~~`````~~~`~`````~`~``~` 3
         4 ~`~~~~`~~`~~`C`~``~~`~~~`~```~``~ 4

           012345678901234567890123456789012
                     1         2         3
    (In the real game, the chests are not visible in the ocean.)

    Press enter to continue...""")
    input()

    print("""
    When you drop a sonar device directly on a chest, you retrieve it
    and the other sonar devices update to show how far away the next nearest
    chest is. The chests are beyond the range of the sonar device on the left,
    so it shows an X.

                     1         2         3
           012345678901234567890123456789012

         0 ~~~~`~```~`~``~~~``~`~~``~~~``~`~ 0
         1 ~`~`~``~~`~```~~~```~~`~`~~~`~~~~ 1
         2 `~`X``7`~~~~`C`~~~~`````~~``~~~`` 2
         3 ````````~~~`````~~~`~`````~`~``~` 3
         4 ~`~~~~`~~`~~`C`~``~~`~~~`~```~``~ 4

           012345678901234567890123456789012
                     1         2         3

    The treasure chests don't move around. Sonar devices can detect treasure chests
    up to a distance of 9 spaces. Try to collect all 3 chests before running out
    of sonar devices. Good luck!

    Press enter to continue... """)
    input()




print("S O N A R !")
print()
if input("Would you like to view the instructions? (yes/no) ").lower().startswith("y"):
    show_instructions()

while True:
    sonar_devices = 20
    the_board = get_new_board()
    the_chests = get_random_chests(3)
    print(the_chests)
    draw_board(the_board)
    previous_moves = []

    while sonar_devices > 0:
        print(f"You have {sonar_devices} sonar device(s) left. {len(the_chests)} chest(s) remaining.")

        x, y = enter_player_move(previous_moves)
        previous_moves.append([x, y])

        move_result = make_move(the_board, the_chests, x, y)
        if move_result == False:
            continue
        else:
            if move_result == "You have found a sunken treasure chest!":
                for x, y in previous_moves:
                    make_move(the_board, the_chests, x, y)
            draw_board(the_board)
            print(move_result)

        if len(the_chests) == 0:
            print("You have found all the sunken treasure chests! Congratulations and good game!")
            break

        sonar_devices -= 1

    if sonar_devices == 0:
        print("We've run out of sonar devices! Now we have to turn the ship around and head")
        print("for home with treasure chests still out there! Game over.")

        print("    The remaining chests were here:")
        for x, y in the_chests:
            print((x, y))

    print("Do you want to play again? (yes or no)")
    if not input().lower().startswith("y"):
        sys.exit()
