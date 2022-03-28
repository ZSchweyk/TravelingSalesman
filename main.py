from itertools import combinations

from selenium.webdriver.common.by import By

from node_class import Node
from tsp_class import TravelingSalesman

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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

browser = webdriver.Firefox()
browser.get("https://maps.google.com")
search_box = browser.find_element(value="searchboxinput")

for combination in all_combinations:
    search_box.send_keys(f"{combination[0]} to {combination[1]}")
    search_box.send_keys(Keys.ENTER)

    browser.find_element(by=By.jstcache, value="1115")





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
print(tsp.brute_force(start=a, method="distance"))
