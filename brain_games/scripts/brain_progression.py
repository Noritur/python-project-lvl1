#!/usr/bin/env python3
from brain_games.cli import welcome_brain_games
from brain_games.games.func_progression import progression_game


def main():
    welcome_brain_games()
    progression_game()


if __name__ == '__main__':
    main()
