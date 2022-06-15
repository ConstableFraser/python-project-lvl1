from random import randint
from brain_games import cli
from brain_games.scripts.game_engine import start_game


def main():
    name = cli.welcome_user()
    print("Answer \"yes\" if the number is even, otherwise answer \"no\"")
    start_game("even", name)


def question():
    number = randint(1, 100)
    print(f"Question: {number}")
    return number


def check_value(value, user_value):
    if value % 2 == 0:
        r = "yes"
    else:
        r = "no"
    return (True, r) if user_value == r else (False, r)


if __name__ == "__main__":
    main()
