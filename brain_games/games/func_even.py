from random import randint

GAME_TERMS = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even_game(question):
    if question % 2 == 0:
        return 'yes'
    return 'no'


def logic_game():
    question = randint(1, 200)
    correct_answer = is_even_game(question)
    return question, correct_answer
