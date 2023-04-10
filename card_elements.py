import os
import random
from enum import Enum


class Suit(Enum):
    HEARTS = 1
    DIAMONDS = 2
    CLUBS = 3
    SPADES = 4


class Rank(Enum):
    ACE = (1, 11)
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13


class Card:

    def __init__(self, suit: Suit, rank: Rank):
        self.suit = suit
        self.rank = rank
        self.width = 80
        self.height = 100
        root_dir = os.path.dirname(os.path.abspath(__file__))

        if any(rank == r for r in [Rank.ACE, Rank.JACK, Rank.QUEEN, Rank.KING]):
            self.front_image_path = os.path.join(root_dir, 'resource', 'images', "cards",
                                                 f"{rank.name.lower()}_of_{suit.name.lower()}.png")

            # self.image_path = f"resource/images/cards/{rank.name.lower()}_of_{suit.name.lower()}.png"
        else:
            # getting the full absolute path
            self.front_image_path = os.path.join(root_dir, 'resource', 'images', "cards",
                                                 f"{rank.value}_of_{suit.name.lower()}.png")
            # relative path is not working
            # self.image_path = f"resource/images/cards/{rank.value}_of_{suit.name.lower()}.png"

        self.back_image_path = os.path.join(root_dir, 'resource', 'images', "cards", "back.png")

    def __str__(self):
        return f"{self.rank.name} of {self.suit.name}"


class Deck:
    def __init__(self, number_of_deck: int = 1):
        self.cards = [Card(suit, rank) for _ in range(number_of_deck) for suit in Suit for rank in Rank]
        root_dir = os.path.dirname(os.path.abspath(__file__))
        self.back_image_path = os.path.join(root_dir, 'resource', 'images', "cards", "back.png")

    def add__cards(self, cards):
        self.cards.extend(cards) if isinstance(cards, list) else self.cards.append(cards)

    def remove_card(self):
        return self.cards.pop(0)

    def shuffle(self):
        random.shuffle(self.cards)

    def check_remaining_cards_count(self, players: int):
        return len(self.cards) >= (players * 2)

    def get_cards_count(self):
        return len(self.cards)

    # def get_played_cards_count(self):
    #     return len(self.played_cards)
