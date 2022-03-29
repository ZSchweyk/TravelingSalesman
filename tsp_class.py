import sys

from node_class import Node
from itertools import permutations


class TravelingSalesman:
    def __init__(self, nodes: list[Node]):
        self.nodes = nodes
        self.visited = []

    def brute_force(self, **kwargs):
        convert_str_to_node = lambda string: [node for node in self.nodes if node.name == kwargs[string]][0]
        if isinstance(kwargs["start"], str):
            start = convert_str_to_node("start")
        else:
            start = kwargs["start"]
        if isinstance(kwargs["end"], str):
            end = convert_str_to_node("end")
        else:
            end = kwargs["end"]

        method = kwargs["method"]
        all_permutations = list(permutations([node for node in self.nodes if node != start and node != end]))
        print("Number of Permutations:", len(all_permutations))
        paths = {}

        count = 1
        for permutation in all_permutations:
            sys.stdout.write(f"\r{round(count/len(all_permutations) * 100, 2)}% Complete")
            count += 1

            total_cost = 0
            for i in range(len(permutation)):
                if i == len(permutation) - 1:
                    break
                current_node: Node = permutation[i]
                next_node: Node = permutation[i+1]
                total_cost += current_node.branches[next_node][method]

            total_cost += start.branches[permutation[0]][method] + permutation[-1].branches[end][method]
            paths[permutation] = total_cost

        print()
        print("Finding shortest path...")
        shortest_path = min(paths, key=paths.get)
        shortest_path_cost = paths[shortest_path]
        return [start] + list(shortest_path) + [end], shortest_path_cost




