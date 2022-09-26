import prompt  # Prompt and verify user input on the command line.


def welcome_brain_games():
    print('Welcome to the Brain Games!')


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


name = prompt.string('May I have your name? ')


prime_terms = 'Answer "yes" if given number is prime. Otherwise answer "no".'


when_wrong_answer = ' is wrong answer ;(. Correct answer was '


even_terms = 'Answer "yes" if the number is even, otherwise answer "no".'


gcd_terms = 'Find the greatest common divisor of given numbers.'


calc_terms = 'What is the result of the expression?'


progression_terms = 'What number is missing in the progression?'
