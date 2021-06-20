from chickenInvadersGame import Game
from goodPlayer import GoodPlayer


def main():
    hero = GoodPlayer(350, 400)
    game = Game(hero)
    game.game_menu()


if __name__ == "__main__":
    main()
