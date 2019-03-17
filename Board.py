import random


class Board:


    def initial_state(self , size = 4):
        queen_position = []
        for i in range(size):
            queen_position.append(random.randint(0, size-1))

        board = []

        for i in range(size):
            aux = []
            for j in range(size):
                aux.append(0)
            board.append(aux)

        for i in range(size):
            board[queen_position[i]][i] = 1


        return board

