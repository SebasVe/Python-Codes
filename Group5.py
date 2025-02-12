# Sydney Agbakoba & Sebastian Vela
# Febuary 13, 2024
import random
import check_input
import sys

def display_board(board):
    print('  1 2 3 4 5')
    for i, row in enumerate(board):
        print(chr(65 + i), "".join(row))



def reset_game():
    print("Displaying the solution to your previous game...")
    # Display the original solution grid (with the hidden ship positions)
    for row in solution:
        print(" ".join(row))

    print("Resetting game...")

    # Reinitialize the board and solution
    board = [['~ '] * 5 for _ in range(5)]
    solution = [[' '] * 5 for _ in range(5)]

    # Randomly place the 2x2 ship again
    row = random.randint(0, 3)
    col = random.randint(0, 3)
    for r in range(row, row + 2):
        for c in range(col, col + 2):
            solution[r][c] = 'S'
    # Show new board
    display_board(board)
    #Restarts the game
    main()




def get_row():
    while True:
        user_input = input("Enter a Row Letter (A-E): ").upper()
        row_mapping = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        if user_input in row_mapping:
            return row_mapping[user_input]
        print("Invalid input. lease enter a letter from A to E.")


def fire_shot(board, solution, row, col):
    return 0


def main():
    board = [['~ '] * 5 for _ in range(5)]
    # Hidden solution grid
    solution = [[' '] * 5 for _ in range(5)]
    # Randomly place the 2x2 ship
    row = random.randint(0, 3)
    col = random.randint(0, 3)
    for r in range(row, row + 2):
        for c in range(col, col + 2):
            # Ship is hidden from player view
            solution[r][c] = 'S'
    #Show initial board
    display_board(board)

    while True:
        print("Menu:")
        print("1. Fire Shot\n2. Show Solution\n3. Quit")
        menu_choice = check_input.get_int_range('',1,3)

        if menu_choice == 1:
            int_fire_row = get_row()
            fire_col = check_input.get_int_range('Enter a Column Number (1-5): ', 1, 5) - 1
            fire_shot(board, solution, int_fire_row, fire_col)
        elif menu_choice == 2:
            reset_game()
        elif menu_choice == 3:
            sys.exit()




main()
