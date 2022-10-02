import math
from random import randint

import prompt
from brain_games.terms_name import gcd_terms, when_wrong_answer


def gcd_game():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(gcd_terms)
    count = 0
    while count <= 2:
        rand_number1 = randint(1, 100)
        rand_number2 = randint(1, 100)
        correct_answer = math.gcd(rand_number1, rand_number2)
        print(f'Question: {rand_number1} {rand_number2}')
        answer = prompt.string('Your answer: ')
        if answer == str(correct_answer):
            print('Correct!')
            count += 1
        else:
            print(f"'{answer}'{when_wrong_answer}'{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    return print(f'Congratulations, {name}!')
