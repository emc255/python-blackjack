import pygame

from animation import Animation
from card_elements import Deck
from game_table import GameTable
from player import Player


def main():
    # initialize screen
    pygame.init()
    screen_width = 800
    screen_height = 600
    screen_background_color = (66, 123, 184)
    screen = pygame.display.set_mode((screen_width, screen_height))

    # initialize game
    player = Player("jessica", 1111)
    deck = Deck()
    game_table = GameTable(player, deck)
    animation = Animation(screen, screen_width, screen_height,
                          screen_background_color, deck.back_image_path)

    # clickable area

    text_start_rect = animation.text_start()

    # start game
    game_table.start()
    animation.start()

    # number of players it includes dealer
    number_of_players = 2

    while True:
        # Check for Pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # If the user clicks the close button, quit Pygame and exit the program
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONUP:
                # Move object to the location where the user clicked
                mouse_pos = pygame.mouse.get_pos()
                print(mouse_pos)
                if text_start_rect.collidepoint(mouse_pos):

                    if deck.check_remaining_cards_count(number_of_players):
                        animation.card_shuffle()
                        game_table.card_shuffle()
                        animation.deal_card(deck.cards, number_of_players)

            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                animation.deal_card(deck.cards, number_of_players)
                game_table.deal_card(number_of_players)


if __name__ == '__main__':
    main()
