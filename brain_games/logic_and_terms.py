import prompt
from brain_games.cli import welcome_user

when_wrong_answer = ' is wrong answer ;(. Correct answer was '


def answers(question, correct_answer):
    print(f'Question: {question}')
    answer = prompt.string('Your answer: ')
    if correct_answer == str(answer):
        print('Correct!')
        return True
    print(f"'{answer}'{when_wrong_answer}'{correct_answer}'.")
    return False


def start(game):
    name = welcome_user()
    print(game.GAME_TERMS)
    count = 0
    while count != 3:
        question, correct_answer = game.logic_game()
        if answers(question, correct_answer):
            count += 1
        else:
            print(f"Let's try again, {name}!")
        return
    else:
        print(f'Congratulations, {name}!')
