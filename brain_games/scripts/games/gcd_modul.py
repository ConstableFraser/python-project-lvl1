from random import randint


PRMPT = "Find the greatest common divisor of given numbers."


def question():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    val = get_gcd(number1, number2)
    return (f"{number1} {number2}", str(val))


def get_gcd(number1, number2):
    mini = min(number1, number2)
    if number1 == number2:
        return number1
    while mini > 1:
        if (number1 % mini) == 0 and (number2 % mini) == 0:
            return mini
        else:
            mini -= 1
    return mini
