from random import randint


PRMPT = "What number is missing in the progression?"


def question():
    start = randint(1, 100)
    step = randint(2, 6)
    num = randint(1, 10)
    val = get_progress(start, step, num)
    return str(val)


def get_progress(start, step, num):
    n = 1
    s = ""
    val = 0
    while n <= 10:
        if n == num:
            s += ".. "
            val = start
            start += step
        else:
            s += str(start)
            start += step
            s += " "
        n += 1
    print(f"{s}")
    return val
