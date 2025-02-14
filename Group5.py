# Sydney Agbakoba & Sebastian Vela
# Febuary 13, 2024
import random
import check_input
import sys

'''Shows the board to the user as well with the rows and columns labeled'''
def display_board(board):
    print('  1 2 3 4 5')
    for i, row in enumerate(board):
        print(chr(65 + i), "".join(row))



'''Will be used to show the solution to the prior game and
then reset and start a new game'''
def reset_game():
    # Display the original solution grid (with the hidden ship positions)

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
    return board, solution
    #Restarts the game
    main()

'''Will be used to ask for what row letter the 
user wants to pick and then turns it into an int'''
def get_row():
    while True:
        user_input = input("Enter a Row Letter (A-E): ").upper()
        row_mapping = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        if user_input in row_mapping:
            return row_mapping[user_input]
        print("Invalid input. lease enter a letter from A to E.")

'''Uses the input from the user to compare their coordinates to that of the board
and solution board to see if they hit or miss'''
def fire_shot(board, solution, row, col):
    if solution[row][col] == 'S':
        board[row][col] = '* '
        solution[row][col] = 'n'
        return True
    elif solution[row][col] != 'S':
        board[row][col] = 'x '
        return False

'''This is the main function where we ask the user what they want to do
and then call the other functions'''
def main():
    board, solution = reset_game()


    #Show initial board
    display_board(board)

    while True:
        print("Menu:")
        print("1. Fire Shot\n2. Show Solution\n3. Quit")
        menu_choice = check_input.get_int_range('',1,3)

        if menu_choice == 1:
            int_fire_row = get_row()
            fire_col = check_input.get_int_range('Enter a Column Number (1-5): ', 1, 5) - 1
            if board[int_fire_row][fire_col] != '~ ':
                print('Invalid input - Already filled')
                display_board(board)
            else:
                ship_hit = fire_shot(board, solution, int_fire_row, fire_col)
                display_board(board)
                if all('S' not in row for row in solution):
                    print('You Win!')
                    board,solution = reset_game()
        elif menu_choice == 2:
            print('  1 2 3 4 5')
            for i, row in enumerate(solution):
                # Replace ' ' with '~ ' and 'S ' with '* ' before printing
                
                display_row = ['~ ' if cell == ' ' else '* ' for cell in row]
                
                print(chr(65 + i), "".join(display_row))
            print()
            board, solution = reset_game()
        elif menu_choice == 3:
            sys.exit()
main()
