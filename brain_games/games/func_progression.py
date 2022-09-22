from random import randint

import prompt

from brain_games.cli import progression_terms


def progression_game():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    progression_terms()
    count = 0
    while count <= 2:
        random_num_1 = randint(3, 10)
        random_num_2 = randint(80, 100)
        random_progress = randint(1, 5)
        answer = []
        question_number = range(random_num_1, random_num_2, random_progress)
        for numbers_correct in question_number:
            answer.append(numbers_correct)
        answer.sort
        right_answer = randint(0, 9)
        correct_answer = answer[right_answer]
        answer[right_answer] = '...'
        question = ' '.join(map(str, answer[0:10]))
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == str(correct_answer):
            print('Correct!')
            count += 1
        else:
            return print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {name}!")
    return print(f'Congratulations, {name}!')
