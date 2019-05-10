from Game import Game
from AiPlayer import AiPlayer
from HumanPlayer import HumanPlayer

Game(AiPlayer('samsung', False), HumanPlayer('사람', True)).start_loop()
