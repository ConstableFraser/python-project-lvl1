#!/usr/bin/env python

import prompt
ATTEMPT_COUNT = 3


def run_game(get_pair_qa, TEXT_QUEST):
    ncounter = 0
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(TEXT_QUEST)
    while ncounter < ATTEMPT_COUNT:
        question, correct_answer = get_pair_qa()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")
        if user_answer == correct_answer:
            ncounter += 1
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(.", end='')
            print(f" Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
