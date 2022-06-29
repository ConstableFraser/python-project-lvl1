from random import randint
from brain_games.check_correct import is_prime


TEXT_QUEST = "Answer \"yes\" if given number is prime. Otherwise answer \"no\"."
PRIME_MIN = 2
PRIME_MAX = 101


def get_pair_qa():
    number = randint(PRIME_MIN, PRIME_MAX)
    prime = "yes" if is_prime(number) is True else "no"
    return f"{number}", prime
