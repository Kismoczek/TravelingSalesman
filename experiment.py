import mlrose
import random
import numpy as np

# city list
city_coords = [(1, 1), (4, 2), (5, 2), (6, 4), (4, 4), (3, 6), (1, 5), (2, 3)]

# city_coords.append((random.randint(1,10), random.randint(1,10)))
# print(city_coords)

problem = mlrose.TSPOpt(length = 8, coords = city_coords,
                               maximize=False)

best_state, best_fitness = mlrose.genetic_alg(problem, mutation_prob = 0.2,
					      max_attempts = 100, random_state = 2)

print('The best state found is: ', best_state)

print('The fitness at the best state is: ', best_fitness)

# to jest kod skopiowany ze strony, byłoby fajnie jakby działał, ale mój komputer nie radzi sobie z tym pakietem :((
# https://towardsdatascience.com/solving-travelling-salesperson-problems-with-python-5de7e883d847
