from random import randint

GAME_TERMS = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even_game(random_number):
    if random_number % 2 == 0:
        return 'yes'
    return 'no'


def logic_game():
    random_number = randint(1, 200)
    correct_answer = is_even_game(random_number)
    return random_number, correct_answer
