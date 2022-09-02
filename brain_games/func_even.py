from random import randint

import prompt


def brain_games():
    print('Welcome to the Brain Games!')


def even_game():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
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
            print(f"{answer} is wrong answer ;(. Correct answer was {even_or_not}.\nLet's try again, {name}!")
            return
    return print(f'Congratulations, {name}!')
