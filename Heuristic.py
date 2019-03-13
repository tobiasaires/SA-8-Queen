

class Heuristic:

    def __init__(self, board):

        self.board = board
        self.colision = [0]*len(board)
        self.queens_position = []

    def get_queens_postions(self):

        board = self.board

        self.queens_position = []

        for c in range(len(board)):
            for l in range(len(board)):
                if board[l][c] == 1:
                    self.queens_position.append(l)

        return self.queens_position



    def verify_horizontal(self, qp):
        for i in range(len(qp)):
            for j in range(len(qp)):
                if qp[i] == qp[j] and i!=j:
                    self.colision[i] = 1
                    self.colision[j] = 1

        return self.colision