# import random
# import time
from itertools import combinations
from node_class import Node
from tsp_class import TravelingSalesman
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import selenium.common.exceptions
from selenium.webdriver.chrome.options import Options

# https://distancecalculator.globefeed.com/US_Distance_Calculator.asp

with open('locations.txt', 'r') as file:
    all_locations = file.read().replace("\n", ";")
    all_locations = all_locations.split(sep=";")


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


options = Options()
options.headless = True
# options.binary_location = ""

browser = webdriver.Chrome(options=options)
browser.get("https://distancecalculator.globefeed.com/US_Distance_Calculator.asp")

loc1_field = browser.find_element(by=By.ID, value="placename1")
loc2_field = browser.find_element(by=By.ID, value="placename2")
submit_button = browser.find_elements(by=By.TAG_NAME, value="button")[1]

Node.bi_directional = True
location_nodes = [Node(location) for location in all_locations]
all_combinations = list(combinations(location_nodes, 2))

for location in location_nodes:
    for combination in all_combinations:
        if location == combination[0]:
            print(f"Calculating distance between {location.name} and {combination[1].name}...")
            loc1_field.send_keys(location.name)
            # webdriver.ActionChains(browser).send_keys(Keys.ESCAPE).perform()
            loc2_field.send_keys(combination[1].name)
            # webdriver.ActionChains(browser).send_keys(Keys.ESCAPE).perform()
            submit_button.click()

            # New Page with Results
            while True:
                try:
                    driving_distance = float(
                        browser.find_element(by=By.ID, value="drvDistance").text.split()[0])  # miles
                    driving_duration = browser.find_element(by=By.ID, value="drvDuration").text
                    driving_duration = get_hours(driving_duration)
                    location.cost_to(combination[1], distance=driving_distance, time=driving_duration)
                    break
                except:
                    continue

            browser.back()

            while True:
                try:
                    loc1_field = browser.find_element(by=By.ID, value="placename1")
                    loc2_field = browser.find_element(by=By.ID, value="placename2")
                    submit_button = browser.find_elements(by=By.TAG_NAME, value="button")[1]
                    break
                except selenium.common.exceptions.NoSuchElementException:
                    continue

graph = TravelingSalesman(location_nodes)
print("Created graph")
print("Starting brute force algorithm...")
shortest_path = graph.brute_force(
    start="University of Rochester",
    end="University of Rochester",
    methods=["time", "distance"]
)
print(shortest_path)
