from Hanoi import Hanoi
from random import randint

class Individual:
    def __init__(self, tower_len, dna_len, initialize=False):
        self._dna = []
        self._tower = Hanoi(tower_len)
        if dna_len < 2**tower_len-1:
            raise Exception("dna_len must be greater or equal than " + str(2**tower_len-1))
        self._dna_len = dna_len
        if initialize:
            self._initialize()

    def _initialize(self):
        for i in range(self._dna_len):
            selN = randint(0, 2)
            toN = randint(0, 2)
            while selN == toN:
                toN = randint(0, 2)
            self._dna.append({"sel": selN, "to": toN})

    def set_movements(self):
        self._tower.set_movements(self._dna)

    def get_fitness(self):
        tower = self._tower.tower[2]
        fitness_cont = 0
        percent = 100 / len(tower)
        towerCont = 2*len(self._tower.tower[2]) - 1

        for i in range(len(self._tower.tower[2])-1, -1, -1):
            if self._tower.tower[2][i] == towerCont:
                fitness_cont += 1
                towerCont -= 2
            else:
                break

        return percent * fitness_cont