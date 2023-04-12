from game import Game
from player import Player


def main():
    player = Player("jessica", 1220)
    game = Game(player, 1)
    game.start()


if __name__ == '__main__':
    main()
