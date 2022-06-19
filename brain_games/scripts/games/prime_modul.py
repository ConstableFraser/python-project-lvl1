from random import randint


PRMPT = "Answer \"yes\" if given number is prime. Otherwise answer \"no\"."


def question():
    number = randint(2, 101)
    print(f"Question: {number}")
    val = is_prime(number)
    return val


def check_value(value, user_value):
    return (True, value) if value == user_value else (False, value)


def is_prime(number):
    n = 2
    val = "yes"
    while n < number:
        if n == number:
            continue
        if (number % n) == 0:
            val = "no"
            return val
        n += 1
    return val
