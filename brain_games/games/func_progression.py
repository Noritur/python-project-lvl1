from random import randint

GAME_TERMS = 'What number is missing in the progression?'


def logic_game():
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
    return question, correct_answer
