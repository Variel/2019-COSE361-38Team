from Board import Board

class Game:
    def __init__(self, player1, player2):
        self.players= [player1, player2]
        self.current_board = Board()

    def start_loop(self):
        current_state = [False, None]
        current_player = 0
        self.print_state()

        while True:
            while True:
                move = self.players[current_player].next_move(self.current_board)
                if self.current_board.is_valid_move(move):
                    break

                self.current_board = self.current_board.make_move(move, self.players[current_player].identifier)
                current_player = (current_player+1)%2


                self.print_state()
                current_state = self.current_board.determine_state()

                if current_state[0]:
                    break
            print("Winner is "+self.get_player_name((current_state[1])))

    def print_state(self):
        self.current_board._print()
        print("● : {}".format(self.players[0]))
        print("○ : {}".format(self.players[1])+"")

    def get_player_name(self, identifier):

        if identifier is None:
            return "Nobody"
        if identifier is True:
            return self.players[1].Name
        if identifier is False:
            return self.players[0].Name
        return "Nobody"

