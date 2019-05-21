from .Individual import Individual
from random import randint, random

class Population:
    def __init__(self, population_len, tower_len, dna_len, mutation_rate=0.00001, initialize=False):
        self._individuals = []
        self.tower_len = tower_len
        self.dna_len = dna_len

        self.father = None
        self.mother = None

        self.father_fitness = 0
        self.mother_fitness = 0

        self.mutation_rate = mutation_rate

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
            # pp = randint(1, new_population.dna_len-1)
            # genProp = []
            # j = 0
            # for j in range(0, pp):
            #     genProp.append(self.father._dna[j])
            #     if random() < self.mutation_rate:
            #         selN = randint(0, 2)
            #         toN = randint(0, 2)
            #         while selN == toN:
            #             toN = randint(0, 2)
            #         # print("mutation on "+ str(i) +":"+ str(j), selN, toN, end=" - ")
            #         genProp[j]["sel"] = selN
            #         genProp[j]["to"] = toN
            # for k in range(j+1, new_population.dna_len):
            #     genProp.append(self.mother._dna[k])
            #     genProp.append(self.father._dna[j])
            #     if random() < self.mutation_rate:
            #         selN = randint(0, 2)
            #         toN = randint(0, 2)
            #         while selN == toN:
            #             toN = randint(0, 2)
            #         # print("mutation on "+ str(i) +":"+ str(j), selN, toN, end=" - ")
            #         genProp[k]["sel"] = selN
            #         genProp[k]["to"] = toN
            #
            # new_population._individuals[i]._dna = genProp

            for j in range(new_population.dna_len):
                crossRate = randint(0, 1)
                gene = None
                parent = ""
                if (crossRate == 1):
                    gene = self.mother._dna[j]
                    parent = "M"
                else:
                    gene = self.father._dna[j]
                    parent = "F"

                new_population._individuals[i]._dna.append(gene)
                new_population._individuals[i]._dna[j]["parent"] = parent

                if random() < self.mutation_rate:
                    selN = randint(0, 2)
                    toN = randint(0, 2)
                    while selN == toN:
                        toN = randint(0, 2)
                    # print("mutation on "+ str(i) +":"+ str(j), selN, toN, end=" - ")
                    new_population._individuals[i]._dna[j]["sel"] = selN
                    new_population._individuals[i]._dna[j]["to"] = toN
        new_population.set_indiviadual_movements()
        return new_population