from Board import Board

class Game:
    def __init__(self, player1, player2):
        self._players = [player1, player2]
        self._currentBoard = Board()  #### Game.cs 20줄 대신 클래스 인스턴스 변수로 설정.

    def StartLoop(self):

        currentState = [False, None]
        currentPlayer = 0
        self.PrintState()

        while True:
            while True:
                move = self._players[currentPlayer].NextMove(self._currentBoard)
                if self._currentBoard.is_valid_move(move):
                    break;

            self._currentBoard = self._currentBoard.make_move(move, self._players[currentPlayer].Identifier)
            currentPlayer = (currentPlayer + 1) % 2

            self.PrintState()

            currentState = self._currentBoard.determine_state()

            if currentState[0]:
                break

        print("Winner is " + self.GetPlayerName(currentState[1]))



    def PrintState(self):
        self._currentBoard.print()
        print("●: {}\n".format(self._players[0].Name) +
              "○: {}\n".format(self._players[1].Name) +
              "")


    def GetPlayerName(self, identifier):
        if identifier is None:
            return "Nobody"
        if identifier is True:
            return self._players[1].Name
        if identifier is False:
            return self._players[0].Name
        return "Nobody"
