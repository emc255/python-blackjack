import pygame

from game_logic import Game
from player import Player


def main():
    pygame.init()
    window = pygame.display.set_mode((600, 600))
    window.fill((66, 123, 184))
    player = Player("jessica", 1111)
    game = Game(window, player)

    game.start()

    pygame.display.flip()
    while True:
        # Check for Pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # If the user clicks the close button, quit Pygame and exit the program
                pygame.quit()
                quit()


if __name__ == '__main__':
    main()
