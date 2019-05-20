from genetic.Population import Population

generation_cont = 0

if __name__ == "__main__":
    generation = Population(100, 10, 1023, True)
    generation.find_better()
    print(generation.father_fitness, generation.mother_fitness)
    generation = generation.create_new_population_dna()
    generation.find_better()
    print(generation.father_fitness, generation.mother_fitness)
    generation = generation.create_new_population_dna()
    generation.find_better()
    print(generation.father_fitness, generation.mother_fitness)