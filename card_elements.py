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

    def __str__(self):
        return f"{self.rank.name} of {self.suit.name}"


class Deck:
    def __init__(self, number_of_deck: int = 1):
        self.cards = [Card(suit, rank) for _ in range(number_of_deck) for suit in Suit for rank in Rank]
        self.played_cards = []

    def deal_card(self):
        return self.cards.pop()

    def add_played_cards(self, cards):
        if type(cards) == list:
            self.played_cards.extend(cards)
        else:
            self.played_cards.append(cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def get_cards_count(self):
        return len(self.cards)

    def get_played_cards_count(self):
        return len(self.played_cards)
