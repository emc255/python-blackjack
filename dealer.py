from card_elements import Card
from person import Person


class Dealer(Person):
    def __init__(self):
        Person.__init__(self)

    def add_card(self, card: Card):
        super().add_card(card)

    def reset_hand(self):
        return super().reset_hand()

    def calculate_hand_result(self):
        super().calculate_hand_result()
