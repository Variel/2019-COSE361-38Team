from abc import *

class IPlayer(metaclass=ABCMeta):
    name = ""
    identifier = ""

    def __init__(self, name, identifier):
        self.Name = name
        self.Identifier = identifier

    @abstractmethod
    def next_move(self, current_board):
        pass









