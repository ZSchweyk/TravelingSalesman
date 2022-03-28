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
            total_cost = 0
            for i in range(len(permutation)):
                if i == len(permutation) - 1:
                    break
                current_node: Node = permutation[i]
                next_node: Node = permutation[i+1]
                total_cost += current_node.branches[next_node][method]

            total_cost += start.branches[permutation[0]][method] + permutation[-1].branches[start][method]
            paths[permutation] = total_cost

        shortest_path = min(paths, key=paths.get)
        shortest_path_cost = paths[shortest_path]
        return shortest_path, shortest_path_cost




