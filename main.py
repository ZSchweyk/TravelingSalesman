import random
import time
from itertools import combinations

import selenium.common.exceptions

from node_class import Node
from tsp_class import TravelingSalesman
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# https://www.geeksforgeeks.org/python-calculate-distance-duration-two-places-using-google-distance-matrix-api/
# https://distancecalculator.globefeed.com/US_Distance_Calculator.asp


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




browser = webdriver.Chrome()
browser.get("https://distancecalculator.globefeed.com/US_Distance_Calculator.asp")

loc1_field = browser.find_element(by=By.ID, value="placename1")
loc2_field = browser.find_element(by=By.ID, value="placename2")
submit_button = browser.find_elements(by=By.TAG_NAME, value="button")[1]

print(f"{loc1_field=}")
print(f"{loc2_field=}")
print(f"{submit_button=}")

Node.bi_directional = True
college_nodes = [Node(college) for college in colleges]
all_combinations = list(combinations(college_nodes, 2))

for college in college_nodes:
    for combination in all_combinations:
        if college == combination[0]:
            loc1_field.send_keys(college.name)
            # webdriver.ActionChains(browser).send_keys(Keys.ESCAPE).perform()
            loc2_field.send_keys(combination[1].name)
            # webdriver.ActionChains(browser).send_keys(Keys.ESCAPE).perform()
            submit_button.click()

            # New Page with Results

            while True:
                pass
            college.cost_to(combination[1], distance=10, time=10)

graph = TravelingSalesman(college_nodes)
print("Created graph")
print("Starting brute force algorithm...")
shortest_path = graph.brute_force(start="University of Rochester", end="University of Rochester", method="distance")
print("Shortest Path:", shortest_path)

