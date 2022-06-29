from random import randint
from random import choice


TEXT_QUEST = "What is the result of the expression?"
NUMBER1_MIN = 1
NUMBER1_MAX = 100
NUMBER2_MIN = 1
NUMBER2_MAX = 100


def get_pair_qa():
    tuple_operations = ("+", "-", "*")
    number1 = randint(NUMBER1_MIN, NUMBER1_MAX)
    number2 = randint(NUMBER2_MIN, NUMBER2_MAX)
    math_symbol = choice(tuple_operations)
    if math_symbol == '+':
        result = number1 + number2
    elif math_symbol == '-':
        result = number1 - number2
    elif math_symbol == '*':
        result = number1 * number2
    else:
        quit()
    return f"{number1} {math_symbol} {number2}", str(result)
