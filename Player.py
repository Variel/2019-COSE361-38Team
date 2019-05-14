from abc import *

class Player(metaclass=ABCMeta):

    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier

    @abstractmethod
    def next_move(self, current_board):
        pass