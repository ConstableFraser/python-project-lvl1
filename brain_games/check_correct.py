

def is_even(number):
    return True if number % 2 == 0 else False


def is_prime(number):
    n = 2
    while n < number:
        if n == number:
            continue
        if (number % n) == 0:
            return False
        n += 1
    return True
