from card_elements import Deck
from dealer import Dealer
from player import Player


class Game:
    def __init__(self, player: Player, number_of_deck: int = 1):
        self.dealer = Dealer()
        self.player = player
        self.deck = Deck(number_of_deck)
        self.cards_played = []

    def add_played_cards(self, cards):
        if type(cards) == list:
            self.cards_played.extend(cards)
        else:
            self.cards_played.append(cards)

    def start(self):
        self.deck.shuffle()
        play = True
        while play:
            again = input("Again y/n: ")
            if again == "y":
                self.player_bet()
                self.deal_card()
                self.player_turn()
                self.dealer_turn()
                self.check_winners()
                self.reset_hands()
            elif again == "n":
                play = False

    def player_bet(self):
        print(f"{self.player}")
        betting = True
        while betting:
            try:
                amount = float(input("How much do you wanna bet:"))
            except ValueError:
                print("Sorry")
            else:
                if amount > self.player.balance:
                    print("too much")
                else:
                    self.player.add_bet(amount)
                    betting = False

    def deal_card(self):
        players = 2
        if self.deck.check_cards_count(players * 2):
            for _ in range(players):
                self.dealer.add_card(self.deck.remove_card())
                self.player.add_card(self.deck.remove_card())

            print(f"dealer has {self.dealer.reveal_one_card()}")

    def player_turn(self):
        print(f"Your Hand: {self.player.calculate_hand_result()}")
        decision = True
        while decision and len(self.player.cards) < 5:
            result = input("Hit/Stay: ")
            if result.lower() == "stay" or result.lower() == "s":
                decision = False
            if result.lower() == "hit" or result.lower() == "h":
                self.player.add_card(self.deck.remove_card())
                if self.player.calculate_hand_result() > 21:
                    print("Busted")
                    decision = False
                else:
                    print(f"Your Hand: {self.player.calculate_hand_result()}")

    def dealer_turn(self):
        hand_to_beat = self.player.calculate_hand_result()
        dealer_hand = self.dealer.calculate_hand_result()
        if hand_to_beat <= 21:
            print(f"Dealer Hand: {dealer_hand}")
            while dealer_hand < hand_to_beat and dealer_hand <= 21:
                self.dealer.add_card(self.deck.remove_card())
                dealer_hand = self.dealer.calculate_hand_result()
                print(f"Dealer Hand: {dealer_hand}")
        else:
            print(f"Dealer Hand: {dealer_hand}")

    def check_winners(self):
        if self.dealer.calculate_hand_result() > 21:
            print("Everybody wins")
        elif self.dealer.calculate_hand_result() > self.player.calculate_hand_result():
            print("Dealer Wins")
        elif self.player.calculate_hand_result() > self.dealer.calculate_hand_result():
            self.player.add_balance(self.player.bet)
            print("Player Wins")

    def reset_hands(self):
        self.cards_played.extend(self.dealer.cards)
        self.cards_played.extend(self.player.cards)
        self.dealer.reset_hand()
        self.player.reset_hand()
        self.player.reset_bet()
