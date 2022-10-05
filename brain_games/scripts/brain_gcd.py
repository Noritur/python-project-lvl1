#!/usr/bin/env python3
from brain_games.cli import welcome_brain_games
from brain_games.games import func_gcd
from brain_games.logic_and_terms import start


def main():
    welcome_brain_games()
    start(func_gcd)


if __name__ == '__main__':
    main()
