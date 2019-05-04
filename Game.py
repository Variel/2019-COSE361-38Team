import Board
import BoardState

class Game:
    def __init__(self, player1, player2):
        self._players = [player1, player2]
        self._currentBoard = Board()  #### Game.cs 20줄 대신 클래스 인스턴스 변수로 설정.

    def StartLoop(self):

        currentState = BoardState()
        currentPlayer = 0
        self.PrintState()

        while True:
            while True:
                move = self._players[currentPlayer].NextMove(self._currentBoard)
                if not self._currentBoard.IsValidMove(move):
                    continue
                break
            self._currentBoard = self._currentBoard.MakeMove(move, self._players[currentPlayer].Identifier)
            currentPlayer = (currentPlayer + 1) % 2
            self.PrintState()
            currentState = self._currentBoard.DetermineState()
            if not currentState.IsOver:
                continue
            break

        print("Winner is " + self.GetPlayerName(currentState.WinnerIdentifier))



    def PrintState(self):
        self._currentBoard.Print()
        print("●: {}\n".format(self._players[0].Name) +
              "○: {}\n".format(self._players[0].Name) +
              "")


    def GetPlayerName(self, identifier):
        # if not identifier.HasValue:
        #     return "Nobody"
        #### 윗 부분은 어떻게 처리해야할지 모르겠습니다. 생략가능한가요?
        if identifier is True:  #### 기존 코드와 조금 다릅니다. 맞는지는 모르겠어요.
            return self._players[1].Name
        if identifier is False:
            return self._players[0].Name
        return "Nobody"



