from random import choice, randint

import prompt
from brain_games.terms_name import calc_terms, when_wrong_answer


def calc_game():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(calc_terms)
    count = 0
    while count <= 2:
        operator = ['-', '+', '*']
        random_operator = choice(operator)
        random_number1 = randint(1, 100)
        random_number2 = randint(1, 100)
        question = f'{random_number1} {random_operator} {random_number2}'
        correct_answer = eval(question)
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == str(correct_answer):
            print('Correct!')
            count += 1
        else:
            print(f"'{answer}'{when_wrong_answer}'{correct_answer}'.")
            print(f"Let's try again, {name}!")
    return print(f'Congratulations, {name}!')
