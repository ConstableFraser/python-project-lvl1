from random import randint


TEXT_ANSWER = "What number is missing in the progression?"
ROUND_COUNT = 10
INIT_MIN = 1
INIT_MAX = 100
COMMON_DIFFERENCE_MIN = 2
COMMON_DIFFERENCE_MAX = 6
SECRET_POSITION_MIN = 1
SECRET_POSITION_MAX = 10


def get_question_answer():
    initial_term = randint(INIT_MIN, INIT_MAX)
    common_difference = randint(COMMON_DIFFERENCE_MIN, COMMON_DIFFERENCE_MAX)
    secret_position = randint(SECRET_POSITION_MIN, SECRET_POSITION_MAX)
    sequence = get_sequence(initial_term, common_difference, ROUND_COUNT)
    secret = sequence[secret_position]
    return to_string(sequence, secret_position), str(secret)


def get_sequence(initial_term, common_difference, size):
    sequence = []
    sequence.append(str(initial_term))
    while len(sequence) <= size:
        initial_term += common_difference
        sequence.append(str(initial_term))
    return sequence


def to_string(sequence, secret_position):
    sequence[secret_position] = ".."
    string = " ".join(sequence)
    return string
