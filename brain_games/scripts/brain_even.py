#!/usr/bin/env python3
from brain_games.cli import welcome_brain_games
from brain_games.games.func_even import even_game


def main():
    welcome_brain_games()
    even_game()


if __name__ == '__main__':
    main()
