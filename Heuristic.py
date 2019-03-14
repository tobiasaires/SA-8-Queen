

class Heuristic:

    def __init__(self, board):

        self.board = board
        self.attack = 0
        self.queens_position = []



    def get_queens_postions(self):

        board = self.board

        self.queens_position = []

        for c in range(len(board)):
            for l in range(len(board)):
                if board[l][c] == 1:
                    self.queens_position.append(l)

        return self.queens_position

    def attacks(self):
        self.verify_main_diagonal(self.board, self.get_queens_postions())
        self.verify_secondary_diagonal(self.board, self.get_queens_postions())
        self.verify_horizontal(self.board, self.get_queens_postions())

        return self.attack


    def verify_main_diagonal(self, board, qp):

        for c in range(len(qp)):
            line = qp[c]
            column = c
            while column < len(qp) and line < len(qp):
                if board[line][column] == 1 and column != c and line != qp[c]:
                    self.attack += 1
                line += 1
                column += 1
        return self.attack


    def verify_secondary_diagonal(self, board, qp):

        for c in range(len(qp)):
            line = qp[c]
            column = c
            while column >= 0 and line < len(qp):
                if board[line][column] == 1 and column != c and line != qp[c]:
                    self.attack += 1
                line += 1
                column -= 1
        return self.attack

    def verify_horizontal(self, board, qp):
        for i in range(len(board)):
            current = 0
            while(current < i):
                if board[qp[i]][current] == 1:
                    self.attack += 1
                current += 1


        return self.attack