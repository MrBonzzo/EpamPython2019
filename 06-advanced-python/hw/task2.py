"""
E - dict(<V> : [<V>, <V>, ...])
Ключ - строка, идентифицирующая вершину графа
значение - список вершин, достижимых из данной

Сделать так, чтобы по графу можно было итерироваться(обходом в ширину)

"""

from collections import deque


class Graph:
    def __init__(self, E):
        self.E = E

    def __iter__(self):
        self.vertice_queue = deque(sorted(list(self.E))[0])
        self.vertice_queue = deque('C')
        self.passed_vertice = set()
        return self

    def __next__(self):
        while self.vertice_queue:
            current_vertice = self.vertice_queue.popleft()
            if current_vertice not in self.passed_vertice:
                self.vertice_queue.extend(self.E[current_vertice])
                self.passed_vertice.add(current_vertice)
                return current_vertice
        if set(self.E) == self.passed_vertice:
            raise StopIteration
        unpassed_vertice = sorted(list(set(self.E) - self.passed_vertice))
        self.vertice_queue.append(unpassed_vertice[0])
        return self.__next__()


E = {'A': ['B', 'C', 'D'], 'B': ['C'], 'C': [], 'D': ['A']}
graph = Graph(E)

for vertice in graph:
    print(vertice)
