import random

# Objective function: f(x) = x^2
def fitness(x):
    return x ** 2

# Parameters
population_size = 6      # Number of individuals in each generation
chromosome_length = 5    # Number of bits (since 2^5 = 32 possible values)
generations = 10         # Number of generations to evolve
mutation_rate = 0.1      # Probability of mutation

# Generate initial population (random binary strings)
def generate_population():
    population = []
    for _ in range(population_size):
        chromosome = ''.join(random.choice(['0', '1']) for _ in range(chromosome_length))
        population.append(chromosome)
    return population

# Decode binary string to integer
def decode(chromosome):
    return int(chromosome, 2)

# Selection: choose two parents using tournament selection
def select(population):
    selected = random.sample(population, 2)
    return max(selected, key=lambda c: fitness(decode(c)))

# Crossover: single-point crossover between two parents
def crossover(parent1, parent2):
    point = random.randint(1, chromosome_length - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

# Mutation: flip bits randomly
def mutate(chromosome):
    new_chromosome = ''
    for bit in chromosome:
        if random.random() < mutation_rate:
            new_chromosome += '1' if bit == '0' else '0'
        else:
            new_chromosome += bit
    return new_chromosome

# Genetic Algorithm main function
def genetic_algorithm():
    population = generate_population()
    print("Initial Population:", population)

    for gen in range(generations):
        new_population = []

        # Create new population
        while len(new_population) < population_size:
            parent1 = select(population)
            parent2 = select(population)
            child1, child2 = crossover(parent1, parent2)
            new_population.append(mutate(child1))
            new_population.append(mutate(child2))

        # Trim to maintain fixed population size
        population = new_population[:population_size]

        # Find best solution in current generation
        best = max(population, key=lambda c: fitness(decode(c)))
        print(f"Generation {gen+1}: Best = {best}, x = {decode(best)}, f(x) = {fitness(decode(best))}")

    # Final best solution
    best = max(population, key=lambda c: fitness(decode(c)))
    print("\nOptimal Solution Found:")
    print(f"Binary: {best}, Decimal: {decode(best)}, f(x) = {fitness(decode(best))}")

# Run the GA
genetic_algorithm()
