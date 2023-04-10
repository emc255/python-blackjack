from abc import ABC, abstractmethod


class GameLogic(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def deal_card(self, *args):
        pass
