#!/usr/bin/env python

import prompt


def run_game(question, PRMPT):
    ncounter = 0
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(PRMPT)
    while ncounter < 3:
        print('Question: ', end='')
        correct = question()
        a = prompt.string("Your answer: ")
        if a == correct:
            ncounter += 1
            print("Correct!")
        else:
            print(f"'{a}' is wrong answer ;(. Correct answer was '{correct}'")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
