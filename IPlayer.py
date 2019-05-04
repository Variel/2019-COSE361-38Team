from abc import *


class IPlayer(metaclass=ABCMeta):
    name = ""
    identifier = ""
    def __init__(self, name, identifier):
        self.Name = name
        self.Identifier = identifier
    def NextMove(self, currentBoard):
        pass









