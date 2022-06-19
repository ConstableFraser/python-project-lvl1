from random import randint


PRMPT = "Answer \"yes\" if the number is even, otherwise answer \"no\""


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
