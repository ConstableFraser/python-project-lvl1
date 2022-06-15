import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    str = prompt.string("May I have your name? ")
    print(f"Hello, {str}!")
    return str
