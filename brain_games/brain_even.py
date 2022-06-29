import brain_games.game_engine
from brain_games.scripts.games.even_modul import get_pair_qa, TEXT_QUEST


def main():
    brain_games.game_engine.run_game(get_pair_qa, TEXT_QUEST)


if __name__ == "__main__":
    main()
