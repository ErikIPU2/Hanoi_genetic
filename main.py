from genetic.Population import Population

generation_cont = 1

if __name__ == "__main__":
    generation = Population(100, 6, 500, initialize=True, mutation_rate=0.01)
    generation.find_better()

    while generation.father_fitness < 100:
        generation_cont += 1
        generation = generation.create_new_population_dna()
        generation.find_better()
        print(generation_cont, generation.father_fitness)
        print("\n" + generation.father._tower.get_graphic(2))

    print(generation.father._dna)
    print(generation.father._tower.get_graphic(2))
