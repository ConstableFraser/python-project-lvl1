from random import randint
from random import choice


PRMPT = "What is the result of the expression?"


def question():
    operation = ("+", "-", "*")
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    char = choice(operation)
    if char == '+':
        result = number1 + number2
    elif char == '-':
        result = number1 - number2
    elif char == '*':
        result = number1 * number2
    else:
        print("System error. Exit")
        quit()
    print(f"Question: {number1} {char} {number2}")
    return result


def check_value(value, user_value):
    return (True, value) if value == int(user_value) else (False, value)
