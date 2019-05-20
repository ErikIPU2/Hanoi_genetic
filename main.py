from genetic.Population import Population

generation_cont = 1

if __name__ == "__main__":
    generation = Population(500, 6, 1000, initialize=True)
    generation.find_better()

    while generation.father_fitness < 100:
        generation_cont += 1
        generation = generation.create_new_population_dna()
        generation.find_better()
        print(generation_cont, generation.father_fitness)

    print(generation.father._dna)
    print(generation.father._tower.get_graphic(2))
