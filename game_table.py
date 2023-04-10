from card_elements import Deck
from dealer import Dealer
from game_logic import GameLogic
from player import Player


class GameTable(GameLogic):
    def __init__(self, player: Player, deck: Deck):
        self.dealer = Dealer()
        self.player = player
        self.deck = deck
        self.cards_played = []

    def add_played_cards(self, cards):
        if type(cards) == list:
            self.cards_played.extend(cards)
        else:
            self.cards_played.append(cards)

    def start(self):
        self.deck.shuffle()

    # def start(self):
    #     self.deck.shuffle()
    #     play = True
    #     while play and self.player.balance > 0:
    #         again = input("Again y/n: ")
    #         if again == "y":
    #             self.player_bet()
    #             self.deal_card()
    #             self.player_turn()
    #             self.dealer_turn()
    #             self.check_winners()
    #             self.reset_hands()
    #         elif again == "n":
    #             play = False

    def player_bet(self):
        print(f"{self.player}")
        betting = True
        while betting:
            try:
                amount = float(input("How much do you wanna bet:"))
            except ValueError:
                print("Sorry")
            else:
                if amount > self.player.balance + 1:
                    print("too much")
                else:
                    self.player.add_bet(amount)
                    betting = False

    def deal_card(self, number_of_players: int):
        for _ in range(number_of_players):
            self.dealer.add_card(self.deck.remove_card())
            self.player.add_card(self.deck.remove_card())

    # def deal_card(self, cards):
    #     is_player_receive_card = True
    #     number_of_cards_to_deal = 4
    #     center_x = (self.screen.get_width() - 80) // 2
    #     center_y = (self.screen.get_height() - 100) // 2
    #     image_x = center_x - 10
    #
    #     back_image = pygame.transform.scale(pygame.image.load("resource/images/cards/back.png").convert(), (80, 100))
    #     self.screen.blit(back_image, (center_x, center_y))
    #
    #     if not self.deck.check_cards_count(number_of_cards_to_deal):
    #         # recursive shuffle the cards then call itself or shuffle before dealing
    #         return
    #
    #     for index in range(number_of_cards_to_deal):
    #         if index == number_of_cards_to_deal - 1:
    #             image = pygame.transform.scale(pygame.image.load(self.deck.cards[index].back_image_path).convert(),
    #                                            (self.deck.cards[index].width, self.deck.cards[index].height))
    #         else:
    #             image = pygame.transform.scale(pygame.image.load(self.deck.cards[index].front_image_path).convert(),
    #                                            (self.deck.cards[index].width, self.deck.cards[index].height))
    #         image_y = center_y - 40
    #         if is_player_receive_card:
    #             self.player.add_card(self.deck.remove_card())
    #             image_y += 140
    #             while image_y < 450:
    #                 image_y += .1
    #                 self.screen.blit(image, (image_x, image_y))
    #                 pygame.draw.rect(self.screen, (66, 123, 184), (image_x, image_y, 80, 100), 1)
    #                 pygame.display.flip()
    #         else:
    #             self.dealer.add_card(self.deck.remove_card())
    #             image_y -= 100
    #             while image_y > 50:
    #                 image_y -= .1
    #                 self.screen.blit(image, (image_x, image_y))
    #                 pygame.draw.rect(self.screen, (66, 123, 184), (image_x, image_y, 80, 100), 1)
    #                 pygame.display.flip()
    #             image_x += 20
    #         is_player_receive_card = not is_player_receive_card
    def player_turn(self):
        decision = True
        while decision and len(self.player.cards) < 5:
            print(f"Your Hand: {self.player.calculate_hand_result()}")
            for a in self.player.cards:
                print(a)
            result = input("Hit/Stay: ")
            if result.lower() == "stay" or result.lower() == "s":
                decision = False
            if result.lower() == "hit" or result.lower() == "h":
                self.player.add_card(self.deck.remove_card())
                if self.player.calculate_hand_result() > 21:
                    print("Player Busted")
                    decision = False

    def dealer_turn(self):
        hand_to_beat = self.player.calculate_hand_result()
        dealer_hand = self.dealer.calculate_hand_result()
        if hand_to_beat <= 21:
            while dealer_hand < hand_to_beat and dealer_hand <= 21:
                print(f"Dealer Hand: {dealer_hand}")
                self.dealer.add_card(self.deck.remove_card())
                dealer_hand = self.dealer.calculate_hand_result()

    def check_winners(self):
        print(f"Dealer Hand: {self.dealer.calculate_hand_result()}")
        if self.dealer.calculate_hand_result() > 21:
            print("Everybody wins")
            self.player.add_balance(self.player.bet)
        elif self.dealer.calculate_hand_result() > self.player.calculate_hand_result():
            print("Dealer Wins")
            self.player.subtract_bet()
        elif self.player.calculate_hand_result() > 21:
            self.player.subtract_bet()
        elif self.player.calculate_hand_result() > self.dealer.calculate_hand_result():
            self.player.add_balance(self.player.bet)
            print("Player Wins")
        else:
            print("Draw")

    def reset_hands(self):
        self.cards_played.extend(self.dealer.cards)
        self.cards_played.extend(self.player.cards)
        self.dealer.reset_hand()
        self.player.reset_hand()
        self.player.reset_bet()
