# Sydney Agbakoba & Sebastian Vela
# Febuary 13, 2024
import random
import check_input

def display_board(board):
    print('  1 2 3 4 5')
    for i, row in enumerate(board):
        print(chr(65 + i), "".join(row))



def reset_game():
    def get_row():
        user_input = input("Enter a Row Letter (A-E):")
        if user_input == "A":
            return 0
        elif user_input == "B":
            return 1
        elif user_input == "C":
            return 2
        elif user_input == "D":
            return 3
        elif user_input == "E":
            return 4
        else:
            print("Invalid Input")
            get_row()
        user_input = input("Enter a Column Number (1-5):")
        if user_input == "1":
            return 0
        elif user_input == "2":
            return 1
        elif user_input == "3":
            return 2
        elif user_input == "4":
            return 3
        elif user_input == "5":
            return 4
        else:
            print("Invalid number:")
            get_row()



def fire_shot(board, solution, row, col):





def main():
    board = [['~ '] * 5 for _ in range(5)]
    display_board(board)
    str_fire_row = ''
    int_fire_row = 0
    fire_col = 0
    print("Menu:")
    print("1. Fire Shot\n2. Show Solution\n3. Quit")
    menu_choice = check_input.get_int('',1,3)
    if menu_choice == 1:
        str_fire_row = input('Enter a Row Letter (A-E): ').upper()
        #This will make the row letter turn into a int index
        if str_fire_row == "A":
            int_fire_row = 0
        elif str_fire_row == "B":
            int_fire_row = 1
        elif str_fire_row == "C":
            int_fire_row = 2
        elif str_fire_row == "D":
            int_fire_row = 3
        elif str_fire_row == "E":
            int_fire_row = 4
        fire_col = check_input.get_int_range('Enter a Column Number (1-5): ',1,5)
        fire_shot(board, solution, int_fire_row, fire_col-1)
    elif menu_choice == 2:
        reset_game()
    elif menu_choice == 3:
        sys.exit()




main()