from .Individual import Individual
from random import randint

class Population:
    def __init__(self, population_len, tower_len, dna_len, initialize=False):
        self._individuals = []
        self.tower_len = tower_len
        self.dna_len = dna_len

        self.father = None
        self.mother = None

        self.father_fitness = 0
        self.mother_fitness = 0

        if population_len <= 0:
            raise Exception("Population len need to be greater than 0")
        self.population_len = population_len
        if initialize:
            self._initialize()

    def _initialize(self):
        for i in range(self.population_len):
            self._individuals.append(Individual(self.tower_len, self.dna_len, initialize=True))
        self.set_indiviadual_movements()

    def set_indiviadual_movements(self):
        for individual in self._individuals:
            individual.set_movements()

    def find_better(self):
        self.father = self._individuals[0]
        self.mother = self._individuals[1]
        for individual in self._individuals:
            if individual.get_fitness() > self.father.get_fitness():
                self.mother = self.father
                self.father = individual
        self.father_fitness = self.father.get_fitness()
        self.mother_fitness = self.mother.get_fitness()

    def create_new_population_dna(self):
        new_population = Population(self.population_len, self.tower_len, self.dna_len)
        for i in range(new_population.population_len):
            new_population._individuals.append(Individual(new_population.tower_len, new_population.dna_len))
            for j in range(new_population.dna_len):
                crossRate = randint(0, 1)
                gene = None
                if (crossRate == 1):
                    gene = self.mother._dna[j]
                else:
                    gene = self.father._dna[j]
                new_population._individuals[i]._dna.append(gene)
        new_population.set_indiviadual_movements()
        return new_population