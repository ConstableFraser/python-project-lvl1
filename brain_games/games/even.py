from random import randint
from brain_games.scripts.check_correct import is_even


RULES = "Answer \"yes\" if the number is even, otherwise answer \"no\""
EVEN_MIN = 1
EVEN_MAX = 100


def get_round():
    number = randint(EVEN_MIN, EVEN_MAX)
    even = "yes" if is_even(number) is True else "no"
    return f"{number}", even
