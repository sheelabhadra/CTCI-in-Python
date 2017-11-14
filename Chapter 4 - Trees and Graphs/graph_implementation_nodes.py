# Graph implementation using nodes
# The graph is directed nd the edges can hold weights
# There are 3 classes, a State class, a Node class, and a Graph class
# We use 2 built-in Python tools `OrderedDict` and `Enum`

from enum import Enum
from collections import OrderedDict

class State(Enum):
	unvisited = 1
	visited = 2
	visiting = 3

class Node:
	def __init__(self,num):
		self.num = num
		self.visit_state = State.unvisited
		self.adjacent = OrderedDict() #key = node, value = weight

	def __str__(self):
		return str(self.num)

class Graph:
	def __init__(self):
		self.nodes = OrderedDict()

	def add_node(self, num):
		node = Node[num]
		self.nodes[num] =  node
		return node

	def add_edge(self, source, dest, weight=0):
		if source not in self.nodes:
			self.add_node(source)
		if dest not in self.nodes:
			self.add_node(dest)

		self.nodes[source].adjacent[self.nodes[dest]] = weight

g = Graph()
g.add_edge(0,1,5)
g.add_edge(1,2,3)
