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






def get_hours(string: str):
    string_list = string.split()
    if len(string_list) == 4:
        hours = int(string_list[0])
        minutes = int(string_list[2])
        return hours + minutes / 60
    elif len(string_list) == 2:
        if string_list[1] == "minutes":
            return int(string_list[0]) / 60
        else:
            return int(string_list[0])

browser = webdriver.Chrome()
browser.get("https://distancecalculator.globefeed.com/US_Distance_Calculator.asp")

loc1_field = browser.find_element(by=By.ID, value="placename1")
loc2_field = browser.find_element(by=By.ID, value="placename2")
submit_button = browser.find_elements(by=By.TAG_NAME, value="button")[1]

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

            time.sleep(2)

            # New Page with Results
            driving_distance = float(
                browser.find_element(by=By.ID, value="drvDistance").text.split()[0])  # miles
            driving_duration = browser.find_element(by=By.ID, value="drvDuration").text.split()
            driving_duration = int(driving_duration[0]) + float(driving_duration[2]) / 60  # hours
            college.cost_to(combination[1], distance=driving_distance, time=driving_duration)

            browser.back()

            time.sleep(2)

            loc1_field = browser.find_element(by=By.ID, value="placename1")
            loc2_field = browser.find_element(by=By.ID, value="placename2")
            submit_button = browser.find_elements(by=By.TAG_NAME, value="button")[1]

            time.sleep(2)

graph = TravelingSalesman(college_nodes)
print("Created graph")
print("Starting brute force algorithm...")
shortest_path = graph.brute_force(start="University of Rochester", end="University of Rochester", method="distance")
print("Shortest Path:", shortest_path)
