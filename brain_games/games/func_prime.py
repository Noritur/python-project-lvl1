from random import randint

import prompt

from brain_games.cli import prime_terms


def prime_game():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    prime_terms()
    count = 0
    while count <= 2:
        random_number = randint(1, 102)
        count_2 = 0
        for i in range(2, random_number // 2 + 1):
            if (random_number % i == 0):
                count_2 += 1
        if (count_2 <= 0):
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ')
        if answer == str(correct_answer):
            print('Correct!')
            count += 1
        else:
            print('Incorrect, try next!')
    return print(f'Congratulations, {name}!')
