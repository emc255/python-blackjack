from abc import ABC, abstractmethod


class GameLogic(ABC):
    @abstractmethod
    def start(self, *args):
        pass

    @abstractmethod
    def deal_card(self, *args):
        pass

    @abstractmethod
    def card_shuffle(self):
        pass
