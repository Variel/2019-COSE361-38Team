import sys

d_row = [0, 1, 1, 1]
d_col = [1, 1, 0, -1]


class Board(object):

    def __init__(self, parent=None):

        self._board_data = [[None] * 7, [None] * 7, [None] * 7, [None] * 7, [None] * 7, [None] * 7]
        self._is_first_movement = True

        if parent is not None:
            self._is_first_movement = parent._is_first_movement
            for i in range(6):
                for j in range(7):
                    self._board_data[i][j] = parent._board_data[i][j]

    def make_move(self, col, value):
        child = Board(self)
        child._is_first_movement = False

        is_valid = False

        for i in range(6):
            if child._board_data[5 - i][col] == None:
                child._board_data[5 - i][col] = value
                is_valid = True
                break

        if not is_valid:
            raise RuntimeError()

        return child

    def is_valid_move(self, col):
        if self._is_first_movement and col == 3:
            return False

        is_valid = False

        for i in range(6):
            if self._board_data[5 - i][col] == None:
                is_valid = True
                break

        return is_valid

    def print(self):
        print('  +--+--+--+--+--+--+--+')
        for i in range(6):
            sys.stdout.write('{} |'.format(6 - i))

            for j in range(7):
                sys.stdout.write(
                    '○' if self._board_data[i][j] == True else '●' if self._board_data[i][j] == False else '  ')
                sys.stdout.write('|')

            print('\n  +--+--+--+--+--+--+--+')
        print('    1  2  3  4  5  6  7')

    def determine_state(self):
        any_space = False

        for i in range(6):
            for j in range(7):
                for k in range(4):
                    if self._board_data[i][j] is not None \
                            and self._is_four_in_a_row(i, j, k):
                        return (True, self._board_data[i][j])

        for i in range(6):
            any_space = any_space or self.is_valid_move(i)

        return (not any_space, None)

    def _is_four_in_a_row(self, row, col, direction, depth=1):

        if depth == 4:
            return True

        val = self._board_data[row][col]

        if val is None:
            return False

        row_to = row + d_row[direction]
        col_to = col + d_col[direction]

        if row_to not in range(6) or col_to not in range(7):
            return False

        if val == self._board_data[row_to][col_to]:
            return self._is_four_in_a_row(row_to, col_to, direction, depth + 1)

        return False
