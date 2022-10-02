from random import randint

import prompt
from brain_games.terms_name import progression_terms, when_wrong_answer


def progression_game():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(progression_terms)
    count = 0
    while count <= 2:
        random_num1 = randint(3, 10)
        random_num2 = randint(80, 100)
        random_progress = randint(1, 5)
        answer = []
        question_number = range(random_num1, random_num2, random_progress)
        for numbers_correct in question_number:
            answer.append(numbers_correct)
        right_answer = randint(0, 9)
        correct_answer = answer[right_answer]
        answer[right_answer] = '..'
        question = ' '.join(map(str, answer[:10]))
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == str(correct_answer):
            print('Correct!')
            count += 1
        else:
            print(f"'{answer}'{when_wrong_answer}'{correct_answer}'.")
            print(f"Let's try again, {name}!")
    return print(f'Congratulations, {name}!')
