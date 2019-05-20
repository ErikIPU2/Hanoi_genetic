from .Individual import Individual

class Population:
    def __init__(self, population_len, tower_len, dna_len, initialize=False):
        self._individuals = []
        self.tower_len = tower_len
        self.dna_len = dna_len
        if population_len <= 0:
            raise Exception("Population len need to be greater than 0")
        self.population_len = population_len
        if initialize:
            self._initialize()

    def _initialize(self):
        for i in range(self.population_len):
            self._individuals.append(Individual(self.tower_len, self.dna_len, initialize=True))