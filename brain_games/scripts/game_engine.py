#!/usr/bin/env python

import prompt


def run_game(question, check_value, PRMPT):
    ncounter = 0
    name = welcome_user(PRMPT)
    while ncounter < 3:
        q = question()
        a = prompt.string("Your answer: ")
        pair = check_value(q, a)
        if pair[0] is True:
            ncounter += 1
            print("Correct!")
        else:
            print(f"'{a}' is wrong answer ;(. Correct answer was '{pair[1]}'")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")


def welcome_user(PRMPT):
    print("Welcome to the Brain Games!")
    str = prompt.string("May I have your name? ")
    print(f"Hello, {str}!")
    print(PRMPT)
    return str
