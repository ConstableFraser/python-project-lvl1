from random import randint


PRMPT = "Find the greatest common divisor of given numbers."


def question():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    print(f"Question: {number1} {number2}")
    val = get_gcd(number1, number2, min((number1, number2)))
    return val


def check_value(value, user_value):
    return (True, value) if value == int(user_value) else (False, value)


def get_gcd(number1, number2, mini):
    if number1 == number2:
        return number1
    if (number1 % mini) == 0 and (number2 % mini) == 0:
        return mini
    else:
        mini = get_gcd(number1, number2, int(mini - 1))
    return mini
