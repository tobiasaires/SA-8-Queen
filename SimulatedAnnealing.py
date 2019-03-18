from Heuristic import Heuristic
from math import exp
import random
from Neighbor import Neighbor



class SimulatedAnnealing:

    def __init__(self, state, iterate, max_disturb, max_success, alpha, start_temp):
        self.iterate = iterate
        self.max_disturb = max_disturb
        self.max_success = max_success
        self.alpha = alpha
        self.start_state = state
        self.neighbor = Neighbor(state)
        self.startTemp = start_temp

    def start(self):
        i = 0
        success = 1
        current_state = self.start_state
        t = self.startTemp

        solutions = []

        while success != 0 and i < self.iterate:
            j = 0
            success = 0
            while success <= self.max_success and j < self.max_disturb:
                f1 = Heuristic(current_state).attacks()
                new_state = self.neighbor.new_state()

                if Heuristic(new_state).attacks() == 0:
                    solutions.append(Heuristic(new_state).get_queens_postions())


                f2 = Heuristic(new_state).attacks()
                delta = f2 - f1
                if not t == 0:
                    if (delta <= 0) or (exp(-delta / t) > random.random()):
                        current_state = new_state
                        success += 1

                j += 1
                self.neighbor = Neighbor(current_state)

                t = self.alpha * t
                i += 1


        aux = []
        for s in solutions:
            if s not in aux:
                aux.append(s)

            return s