from random import randint


PRMPT = "Answer \"yes\" if given number is prime. Otherwise answer \"no\"."


def question():
    number = randint(2, 101)
    prime = is_prime(number)
    return (f"{number}", prime)


def is_prime(number):
    n = 2
    while n < number:
        if n == number:
            continue
        if (number % n) == 0:
            return "no"
        n += 1
    return "yes"
