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
        self.vertice_queue = deque(list(self.E)[0])
        print(self.vertice_queue)
        return self

    def __next__(self):
        while self.vertice_queue:
            current_vertice = self.vertice_queue.popleft()
            self.vertice_queue.extend(self.E[current_vertice])
            return current_vertice
        raise StopIteration


E = {'A': ['B', 'C', 'D'], 'B': ['C'], 'C': [], 'D': []}
graph = Graph(E)

for vertice in graph:
    print(vertice)
