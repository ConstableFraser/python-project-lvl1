from random import randint


PRMPT = "Answer \"yes\" if the number is even, otherwise answer \"no\""


def question():
    number = randint(1, 100)
    even = is_even(number)
    return (f"{number}", even)


def is_even(number):
    if number % 2 == 0:
        return "yes"
    else:
        return "no"
