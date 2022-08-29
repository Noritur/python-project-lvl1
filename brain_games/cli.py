import prompt  # Prompt and verify user input on the command line.


def welcome_user():
    name = prompt.string('May I have your name?')
    print(f'Hello, {name}!')
