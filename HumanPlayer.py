from Player import Player


class HumanPlayer(Player):
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier

    def next_move(self, current_board):
        while True:
            input_col = self.input_col()
            if 1 <= input_col <= 7:
                break
        return input_col - 1

    # 파이썬 내장함수인 input 과 혼동되지 않도록 함수명을 input_col로 변경
    def input_col(self):
        col = 0
        try:
            col = int(input("{0}님, 다음 수를 입력하세요: ".format(self.name)))
        except:
            print("정수를 입력하세요")
            self.input_col()
        return col
