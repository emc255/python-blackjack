from card_elements import Card
from person import Person


class Player(Person):
    def __init__(self, name: str, balance: float):
        super().__init__()
        self.name = name
        self.money = balance

    def add_card(self, card: Card):
        super().add_card(card)

    def reset_hand(self):
        super().reset_hand()

    def calculate_hand_result(self):
        return super().calculate_hand_result()

    def __str__(self):
        return f"{self.name} has a balance of ${self.money:.2f}"
