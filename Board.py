import random

class Board:


    def initial_state(self):
        board_size = 4
        queen_position = []
        for i in range(board_size):
            queen_position.append(random.randint(0, board_size-1))
        print(queen_position)

        board = []

        for i in range(board_size):
            aux = []
            for j in range(board_size):
                aux.append(0)
            board.append(aux)

        for i in range(board_size):
            board[queen_position[i]][i] = 1


        return board


a = Board()

print(a.initial_state())