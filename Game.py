from Board import Board


class Game:
    def __init__(self, player1, player2):
        self._players = [player1, player2]
        self._currentBoard = Board()  #### Game.cs 20줄 대신 클래스 인스턴스 변수로 설정.

    def start_loop(self):

        current_state = [False, None]
        current_player = 0
        self.print_state()

        while True:
            while True:
                move = self._players[current_player].next_move(self._currentBoard)
                if self._currentBoard.is_valid_move(move):
                    break;

            self._currentBoard = self._currentBoard.make_move(move, self._players[current_player].Identifier)
            current_player = (current_player + 1) % 2

            self.print_state()

            current_state = self._currentBoard.determine_state()

            if current_state[0]:
                break

        print("Winner is " + self.get_player_name(current_state[1]))

    def print_state(self):
        self._currentBoard.print()
        print("●: {}\n".format(self._players[0].Name) +
              "○: {}\n".format(self._players[1].Name) +
              "")

    def get_player_name(self, identifier):
        if identifier is None:
            return "Nobody"
        if identifier is True:
            return self._players[1].Name
        if identifier is False:
            return self._players[0].Name
        return "Nobody"
