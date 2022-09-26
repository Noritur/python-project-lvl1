from random import randint

import prompt
from brain_games.terms_and_name import prime_terms, name


def prime_game():
    name
    print(f'Hello, {name}!')
    print(prime_terms)
    count = 0
    while count <= 2:
        random_number = randint(1, 102)
        count2 = 0
        for index in range(2, random_number // 2 + 1):
            if (random_number % index == 0):
                count2 += 1
        if (count2 <= 0):
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ')
        if answer == str(correct_answer):
            print('Correct!')
            count += 1
        else:
            print(f"Let's try again, {name}!")
            return
    return print(f'Congratulations, {name}!')
