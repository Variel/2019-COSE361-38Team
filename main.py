from Game import Game
from AiPlayer import AiPlayer
from HumanPlayer import HumanPlayer

while True:
    try:
        select = int(input('사람 vs AI - 사람이 [1. 선공] or [2. 후공]: '))
        if 1 <= select <= 2:
            break
    except:
        pass
    finally:
        print('1 혹은 2를 입력하세요')

if select == 1:
    player1 = HumanPlayer('사람', False)
    player2 = AiPlayer('인공지능', True)
else:
    player1 = AiPlayer('인공지능', False)
    player2 = HumanPlayer('사람', True)

Game(player1, player2).start_loop()
