from Board import Board
from SimulatedAnnealing import SimulatedAnnealing




def main():

    # size_board = int(input('Defina o tamanho do Tabuleiro: '))
    # interations = int(input('Defina a quantidade de interações do algoritmo: '))
    # max_success = int(input('Defina o numero máximo de sucesso por interação: '))
    # max_disturb = int(input('Defina o numero máximo de pertubação na temperatura: '))
    # temperature = int(input('Defina a temperatura inicial: '))
    # alpha = float(input('Defina o coeficiente de pertubação na temperatura: '))


    init_state = Board().initial_state(8)
    test = SimulatedAnnealing(init_state, 10000, 100, 3, 0.999, 1000).start()


if __name__=='__main__':
    main()

