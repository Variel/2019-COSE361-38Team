import Board
import random
import BoardState
from IPlayer import IPlayer

class AiPlayer(IPlayer):  #### IPlayer를 여기에 쓰는게 맞나요?

    def __init__(self, name, identifier):
        self.Name = name  ####
        self.Identifier = identifier  ####
        self.results =[]  # 각 경우의 수에 따른 휴리스틱 값을 담기 위한 리스트 [(col, sum),(col, sum),(col, sum),(col, sum),(col, sum), (col, sum), (col, sum)]
        self.MaxSimulation = 10000



    def NextMove(self, currentBoard):

        for i in range(7):
            self.results += self.SelectAndSimulate(currentBoard, i, self.MaxSimulation)  #  i 열을 선택하는 경우의 수를 선택한 결과에 대한 휴리스틱 값을 담는다

            return sorted(self.results, reverse=True, key=lambda x: x[1])[0][0]  # 결과 리스트를 리스트 요소의 Value 항목에 대한 내림차순으로 정렬하여 가장 첫번째 요소의 Column 항목을 반환한다. 즉, 가장 높은 휴리스틱 값을 가지는 경우의 수는 어떤 열을 선택한 것인지 반환



    def SelectAndSimulate(self, currentBoard, col, limit):

        if not currentBoard.IsValidMove(col): # 선택한 경우의 수가 둘 수 없는 수인 경우
            return col, -2147483648  #### 파이썬에서 MinValue와 같은 기능이 있는지 몰라서 상수값으로 대신했습니다.

        sum = 0

        for i in range(limit):  # 설정에 따른 시뮬레이션 횟수 만큼 반복
            sum += self.Simulate(currentBoard.MakeMove(col, self.Identifier)) # 시뮬레이션을 돌리고 그 결과를 더한다. 이 때 시뮬레이션 시작 상태는 AI가 이미 col 열에 수를 둔 상태를 시작 상태로 한다.

        return col, sum



    def Simulate(self, currentBoard):
        # 이미 Select 과정에서 내 수는 정해져 있으므로 상대방 차례
        currentPlayer = 0 if self.Identifier else 1
        currentIdentifier = not self.Identifier  ####
        currentState = BoardState()  #### 클라스 참조하는법.....? 맞는듯...

        currentBoard = currentBoard.Makemove()  #### c#의 "do while문"에서 처음 do문은 while조건을 거치지않고 실행된다는 점을 고려해여 while문 전에 미리 이렇게 실행해주었다.
        currentPlayer = (currentPlayer + 1) % 2  # 플레이어 전환
        currentIdentifier = currentPlayer == 1  # 플레이어 전환

        while not currentState.IsOver:  # 시뮬레이션이란 미니 게임을 랜덤으로, 정말 아무렇게나 돌리는 것이다
            check =[None]*7 # "check[move] = True" 할 수 있도록 미리 공간을 만들어놓음.
            move = random.randrange(0, 7) #### c#의 "do while문"에서 처음 do문은 while조건을 거치지않고 실행된다는 점을 고려해여 while문 전에 미리 이렇게 실행해주었다.
            check[move] = True

            while not currentBoard.IsValidMove(move):
                if check == [True, True, True, True, True, True, True]:
                    return 0
                move = random.randrange(0, 7) # 랜덤으로 다음 수 결정
                check[move] = True  # 체크 배열에 체크 해 둠

            currentBoard = currentBoard.Makemove(move, currentIdentifier)

            currentPlayer = (currentPlayer + 1) % 2  # 플레이어 전환
            currentIdentifier = currentPlayer == 1  # 플레이어 전환

            currentState = currentBoard.DetermineState()  # 시뮬레이션 게임의 현재 상태 확인

        if currentState.WinnerIdentifier is self.Identifier:  # 시뮬레이션 게임의 승자가 AiPlayer 개체 본인일 경우
            return 2

        if currentState.WinnerIdentifier is None:  # (null 대신 None 사용) 시뮬레이션 게임의 승자가 없을 경우
            return 0

        if currentState.WinnerIdentifier is not self.Identifier: # AiPlayer 개체 본인이 졌을 경우
            return -1

















