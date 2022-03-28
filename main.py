import time
from itertools import combinations

# from selenium.webdriver.common.by import By

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# colleges = [
#     "Harvard University",
#     "Princeton University",
#     "Yale University",
#     "University of Rochester",
#     "Rochester Institute of Technology",
#     "Johns Hopkins",
#     "Georgia Institute of Technology",
#     "Cornell University",
#     "University of Pennsylvania",
#     "Tufts University",
#     "Duke University",
#     "Brown University",
# ]
#
# all_combinations = list(combinations(colleges, 2))
# print(all_combinations)
#
# browser = webdriver.Chrome()
# browser.get("https://maps.google.com")
# search_box = browser.find_element(value="searchboxinput")
# time.sleep(5)
#
#
# for combination in all_combinations:
#     search_box.send_keys(f"{combination[0]} to {combination[1]}")
#     search_box.send_keys(Keys.ENTER)
#     time.sleep(5)
#
#     # hrs = browser.find_element(by=By.XPATH, value='//*[@jstcache="1115"]/span')
#     hrs = browser.find_element_by_xpath('//span[@jstcache="1115"]')
#     time.sleep(5)
#     print(hrs.text)
#     break


from node_class import Node
from tsp_class import TravelingSalesman


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
print(tsp.better_brute_force(start=a, end=b, method="distance"))
