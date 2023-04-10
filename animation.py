import pygame

from game_logic import GameLogic


class Animation(GameLogic):

    def __init__(self, screen: pygame, screen_width: int, screen_height: int,
                 screen_background_color: tuple, deck_back_image_path: str):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen_background_color = screen_background_color
        self.deck_back_image_path = deck_back_image_path

    def start(self):
        center_x = (self.screen_width - 80) // 2
        center_y = (self.screen_height - 100) // 2
        deck_back_image = pygame.transform.scale(pygame.image.load(self.deck_back_image_path).convert(), (80, 100))
        self.screen.blit(deck_back_image, (center_x, center_y))

    def deal_card(self, cards, number_of_players: int):
        
        is_player_receive_card = True
        number_of_cards_to_deal = 2 * number_of_players
        center_x = (self.screen_width - 80) // 2
        center_y = (self.screen_height - 100) // 2
        image_x = center_x - 10

        for index in range(number_of_cards_to_deal):
            if index == number_of_cards_to_deal - 1:
                image = pygame.transform.scale(pygame.image.load(self.deck_back_image_path).convert(), (80, 100))
            else:
                image = pygame.transform.scale(pygame.image.load(cards[index].front_image_path).convert(),
                                               (cards[index].width, cards[index].height))
            image_y = center_y - 40
            if is_player_receive_card:
                image_y += 140
                while image_y < 450:
                    image_y += .1
                    self.screen.blit(image, (image_x, image_y))
                    pygame.draw.rect(self.screen, (66, 123, 184), (image_x, image_y, 80, 100), 1)
                    pygame.display.flip()
            else:
                image_y -= 100
                while image_y > 50:
                    image_y -= .1
                    self.screen.blit(image, (image_x, image_y))
                    pygame.draw.rect(self.screen, (66, 123, 184), (image_x, image_y, 80, 100), 1)
                    pygame.display.flip()
                image_x += 20
            is_player_receive_card = not is_player_receive_card