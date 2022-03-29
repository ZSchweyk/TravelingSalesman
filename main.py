import random
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
    # "Duke University",
    # "Brown University",
]

Node.bi_directional = True

college_nodes = [Node(college) for college in colleges]

all_combinations = list(combinations(college_nodes, 2))

api_key = "AIzaSyCSjOV-6turv4kdsPNrDY8j-wicM77hbIU"
url ='https://maps.googleapis.com/maps/api/distancematrix/json?'

for college in college_nodes:
    for combination in all_combinations:
        if college == combination[0]:
            r = requests.get(url + 'origins = ' + college.name +
                             '&destinations = ' + combination[1].name +
                             '&key = ' + api_key).json()
            print(r)
            info = r['rows'][0]['elements'][0]

            college.cost_to(combination[1], distance=info["distance"]["value"], time=info["duration"]["value"] / (60 * 60))

graph = TravelingSalesman(college_nodes)
print("Created graph")
print("Starting brute force algorithm...")
shortest_path = graph.brute_force(start="University of Rochester", end="University of Rochester", method="distance")
print("Shortest Path:", shortest_path)

