from random import randint
from brain_games.check_correct import is_even


TEXT_QUEST = "Answer \"yes\" if the number is even, otherwise answer \"no\""
EVEN_MIN = 1
EVEN_MAX = 100


def get_pair_qa():
    number = randint(EVEN_MIN, EVEN_MAX)
    even = "yes" if is_even(number) is True else "no"
    return f"{number}", even
