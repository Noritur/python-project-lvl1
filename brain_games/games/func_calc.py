from random import choice, randint

GAME_TERMS = 'What is the result of the expression?'


def logic_game():
    operator = ['-', '+', '*']
    random_operator = choice(operator)
    random_number1 = randint(1, 100)
    random_number2 = randint(1, 100)
    question = f'{random_number1} {random_operator} {random_number2}'
    correct_answer = str(eval(question))
    return question, correct_answer
