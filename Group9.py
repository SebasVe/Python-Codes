'''Sebastian Vela & Sydney Agbakoba
February 20, 2025
This will be a state and capital quiz program that will run for 10 questions and randomly select different U.S.
states and ask what their capitals are.'''
import random

def read_file_to_dict(file_name):
    states = {}
    with open(file_name, 'r') as file:
        for line in file:
            state, capital = line.strip().split(',')
            states[state] = capital
    return states

def get_random_state(states):
    states_list = list(states.items())
    random_state_int = random.randint(0, len(states_list)-1)
    return states_list[random_state_int]

def get_random_choices(states, correct_capital):
    capitals_list = list(states.values())
    #This takes out the correct captial from the potential wrong answer list
    wrong_choices = [capital for capital in capitals_list if capital != correct_capital]
    #Picks 3 unique answer choices
    random_choices = random.sample(wrong_choices, 3)
    random_choices.append(correct_capital)
    random.shuffle(random_choices)

    return random_choices

def ask_question(correct_state, possible_answers):
    pass


def main():
    print('- State Capitals Quiz -')
    states_dict = read_file_to_dict("statecapitals.txt")


    correct_state_and_capital = get_random_state(states_dict)
    correct_capital = correct_state_and_capital[1]

    print(correct_state_and_capital)
    print(correct_capital)

    wrong_choices = get_random_choices(states_dict, correct_capital)
    print(wrong_choices)

main()

