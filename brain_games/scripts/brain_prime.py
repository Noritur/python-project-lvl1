#!/usr/bin/env python3
from brain_games.cli import welcome_brain_games
from brain_games.games.func_prime import prime_game


def main():
    welcome_brain_games()
    prime_game()


if __name__ == '__main__':
    main()
