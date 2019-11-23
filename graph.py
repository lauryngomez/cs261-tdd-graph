# Graph: An efficient graph.
# A graph implementation that uses an adjacency list to represent vertices
# and edges.
# Your implementation should pass the tests in test_graph.py.
# Lauryn Gomez

import functools

class Graph:

    def __init__(self, data = None):
        self.data = {}

    def adjacent(self, v1, v2):
        return False

    def neighbors(self, vertex):
        return []
    
    def add_vertex(self, vertex):
        if vertex not in self.data:
            self.data[vertex] = []

    def remove_vertex(self, vertex):
        if vertex in self.data:
            del self.data[vertex]

    def add_edge(self, v1, v2):
        pass

    def remove_edge(self, v1, v2):
        pass

