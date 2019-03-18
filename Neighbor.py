from Heuristic import Heuristic
import random

class Neighbor:

    def __init__(self, state):
        self.board = state
        self.base_board = []
        self.queens_postions = Heuristic(self.board).get_queens_postions()

    def create_board(self, queens):
        for i in range(len(self.board)):
            aux = []
            for j in range(len(self.board)):
                aux.append(0)
            self.base_board.append(aux)

        for i in range(len(self.board)):
            self.base_board[queens[i]][i] = 1

        return self.base_board

    def new_state(self):
        queens = self.queens_postions
        num_change = random.randint(1, len(self.board)-1)
        change = []

        for i in range(num_change):
            change.append(random.randint(0, len(self.board)-1))
            x = random.randint(0, len(self.board)-1)
            while( x == queens[change[i]]):
                x = random.randint(0, len(self.board) - 1)
            queens[change[i]] = x


        new_board = self.create_board(queens)

        return new_board

