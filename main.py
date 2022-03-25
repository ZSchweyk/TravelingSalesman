from node_class import Node

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


