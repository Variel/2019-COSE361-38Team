import random
from Board import Board
from IPlayer import IPlayer


class AiPlayer(IPlayer):  #### IPlayer를 여기에 쓰는게 맞나요?

    def __init__(self, name, identifier):
        self.Name = name
        self.Identifier = identifier

        self.max_simulation = 100

    def next_move(self, current_board):
        # 각 경우의 수에 따른 휴리스틱 값을 담기 위한 리스트 [(col, sum), ...]
        results = []

        for i in range(7):
            # i 열을 선택하는 경우의 수를 선택한 결과에 대한 휴리스틱 값을 담는다
            results.append(self.select_and_simulate(current_board, i, self.max_simulation))

        # print(results)
        # input()
        # 결과 리스트를 리스트 요소의 Value 항목에 대한 내림차순으로 정렬하여 가장 첫번째 요소의 Column 항목을 반환한다.
        # 즉, 가장 높은 휴리스틱 값을 가지는 경우의 수는 어떤 열을 선택한 것인지 반환
        return sorted(results, reverse=True, key=lambda x: x[1])[0][0]

    def select_and_simulate(self, current_board, col, limit):

        # 선택한 경우의 수가 둘 수 없는 수인 경우
        if not current_board.is_valid_move(col):
            # 이 경우가 선택 되지 않도록 가장 작은 값으로 설정
            return col, -2147483648

        sum = 0

        # 정해진 시뮬레이션 횟수 만큼 시뮬레이션 반복
        for i in range(limit):
            # 시뮬레이션을 돌리고 그 결과를 더한다.
            # 이 때 시뮬레이션 시작 상태는 AI가 이미 col 열에 수를 둔 상태를 시작 상태로 한다.
            sum += self.simulate(current_board.make_move(col, self.Identifier))

        return col, sum

    def simulate(self, current_board):
        # 이미 Select 과정에서 내 수는 정해져 있으므로 상대방 차례로 초기화
        current_player = 0 if self.Identifier else 1
        current_identifier = not self.Identifier
        current_state = [False, None];

        while not current_state[0]:  # 시뮬레이션이란 미니 게임을 랜덤으로, 정말 아무렇게나 돌리는 것이다
            check = [None] * 7  # "check[move] = True" 할 수 있도록 미리 공간을 만들어놓음.

            move = random.randrange(0, 7)
            check[move] = True

            while not current_board.is_valid_move(move):
                # 랜덤하게 뽑은 모든 경우의 수가 이동 불능일 때
                if check == [True, True, True, True, True, True, True]:
                    # 비겼음
                    return 0

                move = random.randrange(0, 7)  # 랜덤으로 다음 수 결정
                check[move] = True  # 체크 배열에 체크 해 둠

            current_board = current_board.make_move(move, current_identifier)

            current_player = (current_player + 1) % 2  # 플레이어 전환
            current_identifier = current_player == 1  # 플레이어 전환

            # 시뮬레이션 게임의 현재 상태 확인
            current_state = current_board.determine_state()

        # 시뮬레이션 게임의 승자가 AiPlayer 개체 본인일 경우 2
        if current_state[1] is self.Identifier:
            return 2

        # 시뮬레이션 게임의 승자가 없을 경우 0
        if current_state[1] is None:
            return 0

        # AiPlayer 개체 본인이 졌을 경우 -1
        if current_state[1] is not self.Identifier:
            return -1
