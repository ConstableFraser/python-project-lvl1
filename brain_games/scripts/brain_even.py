import brain_games.engine
from brain_games.games.even import get_round, RULES


def main():
    brain_games.engine.run_game(get_round, RULES)


if __name__ == "__main__":
    main()
