from node_class import Node
from itertools import permutations


class TravelingSalesman:
    def __init__(self, nodes: list[Node]):
        self.nodes = nodes
        self.visited = []

    def brute_force(self, **kwargs):
        method = kwargs["method"]
        start: Node = kwargs["start"]
        all_permutations = permutations([node for node in self.nodes if node != start])
        paths = {}

        for permutation in all_permutations:
            for i, node in enumerate(permutation):
                pass




