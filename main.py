import time
from itertools import combinations
import requests, json
# https://www.geeksforgeeks.org/python-calculate-distance-duration-two-places-using-google-distance-matrix-api/

from node_class import Node
from tsp_class import TravelingSalesman


colleges = [
    "Harvard University",
    "Princeton University",
    "Yale University",
    "University of Rochester",
    "Rochester Institute of Technology",
    "Johns Hopkins",
    "Georgia Institute of Technology",
    "Cornell University",
    "University of Pennsylvania",
    "Tufts University",
    "Duke University",
    "Brown University",
]

Node.bi_directional = True

college_nodes = [Node(college) for college in colleges]
print(college_nodes)

all_combinations = list(combinations(college_nodes, 2))
print(all_combinations)

for college in college_nodes:
    for combination in all_combinations:
        if college == combination[0]:
            print("Added cost")
            college.cost_to(combination[1], distance=10, time=10)

graph = TravelingSalesman(college_nodes)
print("Created graph")
print("Starting brute force algorithm...")
shortest_path = graph.brute_force(start="University of Rochester", end="University of Rochester", method="distance")
print("Shortest Path:", shortest_path)

