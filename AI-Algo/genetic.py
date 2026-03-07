import random

def run_genetic():

    def fitness(x):
        return x**2

    population = [random.randint(1,10) for _ in range(6)]

    print("Initial Population:", population)

    for g in range(4):

        population.sort(reverse=True)

        parent1 = population[0]
        parent2 = population[1]

        child = (parent1 + parent2)//2

        child += random.randint(-1,1)

        population[-1] = child

        print("Generation", g+1, ":", population)

    best = max(population)
    print("~Best Solution:", best)
    print("~Fitness:", fitness(best))


print("\nExample 1")
run_genetic()

print("\nExample 2")
run_genetic()