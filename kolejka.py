# KOLEJKA - implementacja i przykład działania
# dodanie kolejki
queue = []
# dodanie elementów do kolejki
queue.append('arbuz')
queue.append('banan')
queue.append('cytryna')
queue.append('daktyl')
queue.append('eukaliptus')

# wygląd wstepnej kolejki ( przed wyjęciem czegokolwiek)
print(queue)

# wyjęcie elementów z kolejki .pop, zawsze wyjmujemy ten najbardziej z góry
print('elements dequeued')
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
# kolejka po zpopowaniu paru pierwszych elementów, pozostają te dodane na końcu
print(queue)
# dodanie elementu na koniec kolejki
queue.append('liczi')
# liczi dalej siedzi na końcu kolejki, popowane są elementy dodane wcześniej
print(queue.pop(0))
# ostateczny wygląd kolejki
print(queue)
