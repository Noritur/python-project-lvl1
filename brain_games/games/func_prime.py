from random import randint

GAME_TERMS = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime_game(random_number):
    for index in range(2, random_number // 2 + 1):
        if random_number % index == 0:
            return 'no'
    return 'yes'


def logic_game():
    random_number = randint(1, 102)
    question = random_number
    correct_answer = str(is_prime_game(random_number))
    return question, correct_answer
