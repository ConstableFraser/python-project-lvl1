#!/usr/bin/env python

import prompt
from brain_games.scripts.games import brain_even
from brain_games.scripts.games import brain_calc


def start_game(func, name):
    ncounter = 0
    while ncounter < 3:
        r = choose_question(func)
        a = prompt.string("Your answer: ")
        p = choose_check(func, r, a)
        if p[0] is True:
            ncounter += 1
            print("Correct!")
        else:
            print(f"'{a}' is wrong answer ;(. Correct answer was '{p[1]}'")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")


def choose_question(func):
    if func == "even":
        return brain_even.question()
    elif func == "calc":
        return brain_calc.question()
    else:
        print("func not found. Exit")
        return None


def choose_check(func, r, answer):
    if func == "even":
        return brain_even.check_value(r, answer)
    elif func == "calc":
        return brain_calc.check_value(r, answer)
    else:
        print("func not found. Exit")
        return None
