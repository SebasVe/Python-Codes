'''Sebastian Vela & Sydney Agbakoba
February 20, 2025
This will be a state and capital quiz program that will run for 10 questions and randomly select different U.S.
states and ask what their capitals are.'''
import random

'''This function will take the name of our file as a parameter and then open it in read mode and iterate through each line
of the file, using the strip and split(',') functions to seperate the states and capitals as keys and values for the dictionary'''
def read_file_to_dict(file_name):
    states = {}
    #We use with to help open and close the file safely
    with open(file_name, 'r') as file:
        #Iterates through each line
        for line in file:
            state, capital = line.strip().split(',')
            states[state] = capital
    return states

'''Here we take the dictionary of states and capitals and then convert it to a list of tuples with the states and capitals, then with the random module
we pick a random index in that list and return it to randomly get back a state and capital pair that we will use for the question and correct answer'''
def get_random_state(states):
    states_list = list(states.items())
    random_state_int = random.randint(0, len(states_list)-1)
    return states_list[random_state_int]

'''We start by making a list of only capitals by calling only the dictionary's values and then in that list we take out the correct capital as a potential wrong
answer choice as well as then randomly selecting three other capitals from that list and appending it the correct capital. Using the shuffle function we then switch around
the choices a bit so that the correct answer isn't always in the same place.'''
def get_random_choices(states, correct_capital):
    capitals_list = list(states.values())
    #This takes out the correct captial from the potential wrong answer list
    wrong_choices = [capital for capital in capitals_list if capital != correct_capital]
    #Picks 3 unique answer choices
    random_choices = random.sample(wrong_choices, 3)
    random_choices.append(correct_capital)
    #Switches around the capitals
    random.shuffle(random_choices)
    return random_choices

'''Here we start by creating a variable to serve as a way to check if the user input is valid later on. Then we print out a statement for the user which will show
four options for capitals in the list that we brought in as a parameter. Then we check if the user's input is between A-D in the while loop and we keep this up
until it is valid. After that we simply check what the user chose and then returning it as an integer.'''
def ask_question(correct_state, possible_answers):
    invalid_user_input = True
    print(f"A. {possible_answers[0]}   B. {possible_answers[1]}   C. {possible_answers[2]}   D. {possible_answers[3]}")
    while invalid_user_input:
        user_selection = input("Enter selection: ").upper()
        if user_selection == 'A' or user_selection == 'B' or user_selection == 'C' or user_selection == 'D':
            invalid_user_input = False
        else:
            print("Invalid input. Input choice A-D.")
    #Checks which input the user chose
    if user_selection == 'A':
        return 0
    elif user_selection == 'B':
        return 1
    elif user_selection == 'C':
        return 2
    elif user_selection == 'D':
        return 3

def main():
    print('- State Capitals Quiz -')
    states_dict = read_file_to_dict("statecapitals.txt")
    question_counter = 1
    user_points = 0
    #Will iterate 10 times and so 10 questions will be displayed
    while question_counter <= 10:
        #Calling our functions to get the lists needed to ask the questions
        correct_state_and_capital = get_random_state(states_dict)
        correct_capital = correct_state_and_capital[1]
        quiz_choices = get_random_choices(states_dict, correct_capital)
        #Here is where the question is actually displayed to the user
        print(f"{question_counter}.  The capital of {correct_state_and_capital[0]} is:")
        user_answer = ask_question(correct_state_and_capital, quiz_choices)
        if quiz_choices[user_answer] == correct_capital:
            print('Correct!')
            user_points += 1
        else:
            print(f"Incorrect! The correct answer is: {correct_capital}")
        question_counter += 1
    #Final display message
    print(f"End of test. You got {user_points} correct.")

main()

