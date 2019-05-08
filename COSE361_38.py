import sys

dRow = [0, 1, 1, 1]
dCol = [1, 1, 0, -1]


class Board(object):
    _boardData = [[None] * 7, [None] * 7, [None] * 7, [None] * 7, [None] * 7, [None] * 7]

    isFirstmove = True

    def MakeMove(self, col, value):
        child = Board(self)
        isvalid = False

        for i in range(5):
            if child._boardData[5 - i][col] is None:
                child._boardData = value
                isValid = True
                break

        if isValid is False:
            print("No")

        return child

    def is_valid_move(self, col):
        if isFirstMove is _boardData[5][3]:
            return false

        isvalid = False

        for i in range(5):
            if child._boardData[5 - i][col] is None:
                isValid = True
            break

        return isValid

    def _print(self):
        print(" +--+--+--+--+--+--+--+--")

        for i in range(6):
            sys.stdout.write('{} |'.format(6 - i))
            for j in range(7):
                if self._boardData[i][j] == True:
                    sys.stdout.write('○')
                if self._boardData[i][j] == False:
                    sys.stdout.write('●')
                else:
                    sys.stdout.write("  ")
            sys.stdout.write('|')

        print("\n +--+--+--+--+--+--+--+--")
        print('    1 2 3 4 5 6 7')

    def DeterMineState(self):
        anyspace = False

        for i in range(6):
            for j in range(7):
                for k in range(4):
                    child._boardData[i][j] == None and self.IsFourInARow(i, j, k)
                    return (True, child.boarData[i][j])

            for i in range(7):
                anyspace = anyspace or is_valid_move(i)

            return (not anyspace, None)

    def IsFourInARow(self, row, col, direction, depth):
        if depth is 4:
            return True

        val = child._boardData[row][col]

        if val is None:
            return False

        rowTo = row + dRow[direction]
        colTo = row + dCol[direction]

        if rowto < 0 or rowTo >= 6 or colTo < 0 or colTo >= 7:
            return False

        if val == child._boardData[rowTo][colTo]:
            return IsFourInARow(rowTo, colTo, direction, depth + 1)

        return False

