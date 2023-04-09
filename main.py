from card_elements import Deck, Card, Suit, Rank
from player import Player


def main():
    deck = Deck(2)
    print(deck.get_cards_count())
    player = Player("jennie", 1200)
    card1 = Card(Suit.DIAMONDS, Rank.ACE)
    card2 = Card(Suit.DIAMONDS, Rank.FIVE)

    player.add_card(card1)
    player.add_card(card2)
    player.add_card(card1)
    print(player.calculate_hand_result())
    player.add_card(card1)
    player.add_card(card1)
    player.add_card(card1)
    player.add_card(card2)
    player.add_card(card2)
    print(player.calculate_hand_result())
    print(player)


main()
