from game import Game
from player import Player

if __name__ == "__main__":
    player = Player("jessica", 1200)
    game = Game(player)
    game.start()
