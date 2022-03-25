from node_class import Node


class TravelingSalesman:
    def __init__(self, nodes: list[Node]):
        self.nodes = nodes
        self.visited = []

    def brute_force(self, **kwargs):
        method = kwargs["method"]
        start = kwargs["start"]
        for node in self.nodes:
            if node not in self.visited:
                pass
