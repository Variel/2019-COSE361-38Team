import sys

d_row = [0,1,1,1]
d_col = [1,1,0,-1]

class Board(object):
    def __init__(self, parent =None):
        self.board_data = [[None]*7,[None]*7,[None]*7,[None]*7,[None]*7,[None]*7]
        self.is_first_move = True

        if parent != None:
            self.is_first_move = parent.is_first_move

            for i in range(6):
                for j in range(7):
                    self.board_data[i][j] = parent.board_data[i][j]

    def make_move(self, col, value):
        child = Board(self)
        child.is_first_move=False
        is_valid = False
        for i in range(6):
            if child.board_data[5-i][col] is None:
                child.board_data[5-i][col]=value
                is_valid = True
                break

        if is_valid is False:
            print("둘 수 없는 곳입니다.")
            raise RuntimeError

        return child


    def is_valid_move(self, col):

        if self.is_first_move and col is 3:
            return False

        is_valid = False

        for i in range(6):
            if self.board_data[5-i][col] is None:
                is_valid = True
                break

        return is_valid

    def _print(self):
        sys.stdout.write("  +--+--+--+--+--+--+--+ \n")

        for i in range(6):
            sys.stdout.write('{} |'.format(6-i))

            for j in range(7):

                if self.board_data[i][j] ==True:
                    sys.stdout.write("○")
                elif self.board_data[i][j]==False:
                    sys.stdout.write("●")
                else :
                    sys.stdout.write("  ")
                sys.stdout.write('|')


            print("\n  +--+--+--+--+--+--+--+")
        print('    1  2  3  4  5  6  7')

    def determine_state(self):
        any_space =False
        for i in range(6):
            for j in range(7):
                for k in range(4):
                    if self.board_data[i][j] != None and self.is_four_in_a_row(i,j,k) is True:
                        return (True, self.board_data[i][j])



        for i in range(6):
            any_space = any_space or self.is_valid_move(i)

        return (not any_space, None)

    def is_four_in_a_row(self, row, col, direction, depth=1):
        if depth is 4:
            return True

        val = self.board_data[row][col]

        if val is None:
            return False

        row_to = row + d_row[direction]
        col_to = col + d_col[direction]

        if(row_to<0 or row_to>=6 or col_to<0 or col_to>=7):
            return False

        if val == self.board_data[row_to][col_to]:
            return self.is_four_in_a_row(row_to, col_to, direction, depth+1)

        return False