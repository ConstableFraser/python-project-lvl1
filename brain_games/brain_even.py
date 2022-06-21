import brain_games.game_engine
from brain_games.scripts.games.even_modul import question, PRMPT


def main():
    brain_games.game_engine.run_game(question, PRMPT)


if __name__ == "__main__":
    main()
