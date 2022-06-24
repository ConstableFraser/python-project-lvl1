from random import randint


PRMPT = "What number is missing in the progression?"


def question():
    initial_term = randint(1, 100)
    common_difference = randint(2, 6)
    secret_position = randint(1, 10)
    sequence = get_sequence(initial_term, common_difference)
    secret = sequence[secret_position]
    return (to_string(sequence, secret_position), str(secret))


def get_sequence(initial_term, common_difference):
    sequence = []
    n = 1
    sequence.append(initial_term)
    while n <= 10:
        initial_term += common_difference
        sequence.append(initial_term)
        n += 1
    return sequence


def to_string(sequence, secret_position):
    string = ""
    n = 0
    while n <= 10:
        if n == secret_position:
            string += ".. "
        else:
            string += str(sequence[n])
            string += " "
        n += 1
    return string
