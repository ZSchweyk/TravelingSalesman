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

all_combinations = list(combinations(colleges, 2))
print(all_combinations)





a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")

Node.bi_directional = True

a.cost_to(b, distance=20, time=20)
a.cost_to(c, distance=10, time=10)
a.cost_to(d, distance=12, time=12)

b.cost_to(c, distance=15, time=15)
b.cost_to(d, distance=11, time=11)

c.cost_to(d, distance=17, time=17)

tsp = TravelingSalesman([a, b, c, d])
print(tsp.brute_force(start=a, end=a, method="distance"))
