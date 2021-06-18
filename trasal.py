import numpy as np
from math import factorial

# liczba miast do wyboru
num_cities = 8
# matryca dystansów
dist_mat = np.random.randint(5, 100, size=(num_cities, num_cities))
dist_mat = (dist_mat + dist_mat.T) // 2
np.fill_diagonal(dist_mat, 0)
# print(dist_mat)

# słownik miast - żeby można było nazwać
cities = {}
for i in range(num_cities):
    cities.update({i: ('city' + str(i + 1))})

# najkrótszy dystans
shortest = {'distance': (num_cities + 1) * 100,
            'used_paths': []}

# pętla do ścieżki
while len(shortest['used_paths']) != factorial(num_cities):
    path = np.random.permutation(num_cities)
    path = np.append(path, path[0])
    break

# wyprintowanie miast po kolei
print('Our path is: ')

for j in range(0, len(cities)):
    city = cities[path[j]]

    print(city)
