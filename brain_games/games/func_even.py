from random import randint

import prompt
from brain_games.terms_and_name import even_terms, when_wrong_answer, name


def even_game():
    name
    print(f'Hello, {name}!')
    print(even_terms)
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
            return print(f'''"{answer}"{when_wrong_answer}'{even_or_not}'.
Let's try again, {name}!''')
    return print(f'Congratulations, {name}!')
