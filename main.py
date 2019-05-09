from Game import Game
from AiPlayer import AiPlayer
from HumanPlayer import HumanPlayer

Game(AiPlayer('samsung', False), HumanPlayer('apple', True)).start_loop()
