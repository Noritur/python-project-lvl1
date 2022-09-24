#!/usr/bin/env python3
from brain_games.cli import welcome_brain_games
from brain_games.games.func_gcd import gcd_game


def main():
    welcome_brain_games()
    gcd_game()


if __name__ == '__main__':
    main()
