from random import randint


RULES = "Find the greatest common divisor of given numbers."
NUMBER1_MIN = 1
NUMBER1_MAX = 100
NUMBER2_MIN = 1
NUMBER2_MAX = 100


def get_round():
    number1 = randint(NUMBER1_MIN, NUMBER1_MAX)
    number2 = randint(NUMBER2_MIN, NUMBER2_MAX)
    val = get_gcd(number1, number2)
    return f"{number1} {number2}", str(val)


def get_gcd(number1, number2):
    while number1 != 0 and number2 != 0:
        if number1 > number2:
            number1 %= number2
        else:
            number2 %= number1
    return number1 + number2
