from Board import Board
from SimulatedAnnealing import SimulatedAnnealing
import time
import random



def main():

    # size_board = int(input('Defina o tamanho do Tabuleiro: '))
    # interations = int(input('Defina a quantidade de interações do algoritmo: '))
    # max_success = int(input('Defina o numero máximo de sucesso por interação: '))
    # max_disturb = int(input('Defina o numero máximo de pertubação na temperatura: '))
    # temperature = int(input('Defina a temperatura inicial: '))
    # alpha = float(input('Defina o coeficiente de pertubação na temperatura: '))

    # aux = []
    # while(True):
    #     init_state = Board().initial_state(8)
    #     alpha = random.random()
    #     m = random.random()*20000
    #     l = random.random()*1000
    #     t = random.random()*1000
    #     for i in range(10):
    #         start = time.time()
    #         test = SimulatedAnnealing(init_state, m, l, 10, alpha, t).start()
    #         if test != []:
    #             aux.append(test)
    #
    #         end = time.time()-start
    #
    #     if len(aux)==10:
    #         print(aux)
    #         print(alpha)
    #         print(m,l,t)
    #         break
    #     else:
    #         aux = []

        for i in range(10):
            aux = []
            c = 0
            init_state = Board().initial_state(8)
            for j in range(10):
                test = SimulatedAnnealing(init_state, 14803, 885, 10, 0.9507383112586437, 936).start()
                if test != []:
                    aux.append(test)
            if len(aux) == 10:
                c += 1
        print(c)




if __name__=='__main__':
    main()

