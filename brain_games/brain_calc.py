import brain_games.game_engine
from brain_games.scripts.games.calc_modul import get_question_answer, TEXT_ANSWER


def main():
    brain_games.game_engine.run_game(get_question_answer, TEXT_ANSWER)


if __name__ == "__main__":
    main()
