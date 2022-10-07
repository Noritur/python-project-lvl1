import math
from random import randint

GAME_TERMS = 'Find the greatest common divisor of given numbers.'


def logic_game():
    rand_number1 = randint(1, 100)
    rand_number2 = randint(1, 100)
    correct_answer = str(math.gcd(rand_number1, rand_number2))
    question = f'{rand_number1} {rand_number2}'
    return question, correct_answer
