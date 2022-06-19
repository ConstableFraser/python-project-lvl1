import brain_games.scripts.game_engine
from brain_games.scripts.games.calc_modul import question, check_value, PRMPT


def main():
    brain_games.scripts.game_engine.run_game(question, check_value, PRMPT)


if __name__ == "__main__":
    main()
