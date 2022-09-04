import prompt  # Prompt and verify user input on the command line.


def welcome_brain_games():
    print('Welcome to the Brain Games!')


def even_terms():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def gcd_terms():
    print('Find the greatest common divisor of given numbers.')


def calc_terms():
    print('What is the result of the expression?')


def welcome_user():
    name = prompt.string('May I have your name?')
    print(f'Hello, {name}!')
