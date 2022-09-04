from random import randint

import math

import prompt

from brain_games.cli import gcd_terms


def gcd_game():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    gcd_terms()
    count = 0
    while count <= 2:
        rand_number_1 = randint(1, 100)
        rand_number_2 = randint(1, 100)
        correct_answer = math.gcd(rand_number_1, rand_number_2)
        print(f'Question: {rand_number_1} {rand_number_2}')
        answer = prompt.string('Your answer: ')
        if answer == str(correct_answer):
            print('Correct!')
            count += 1
        else:
            return print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {name}!")
    return print(f'Congratulations, {name}!')
