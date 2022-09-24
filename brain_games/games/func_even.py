from random import randint

import prompt
from brain_games.cli import even_terms


def even_game():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    even_terms()
    count = 0
    while count <= 2:
        random_number = randint(1, 200)
        print(f'Question: {random_number}')
        if random_number % 2 == 0:
            even_or_not = 'yes'
        else:
            even_or_not = 'no'
        answer = prompt.string('Your answer: ')
        if answer == even_or_not:
            print('Correct!')
            count += 1
        else:
            return print(f"'{answer}' is wrong answer ;(. Correct answer was '{even_or_not}'.\nLet's try again, {name}!")
    return print(f'Congratulations, {name}!')
