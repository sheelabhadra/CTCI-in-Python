# You are given a list of projects and a list of dependencies (which is a list of pairs of
# projects, where the second project is dependent on the first project). All of a project's dependencies
# must be built before the project is. Find a build order that will allow the projects to be built. If there
# is no valid build order, return an error.
# EXAMPLE
# Input:
# projects: a, b, c, d, e, f
# dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
# Output: f, e, a, b, d, c
from collections import defaultdict

class Graph:
	def __init__(self,vertices):
		self.graph = defaultdict(list)
		self.V = vertices

	# Add edge to a graph
	def addEdge(self, u, v):
		self.graph[u].append(v)

	def _display(self):
		for k,v in self.graph.items():
			print("{} : {}".format(k,v))

	def topologicalSortUtil(self,v,visited,stack):
		visited[v] = True
		for i in self.graph[v]:
			if visited[i] == False:
				self.topologicalSortUtil(i,visited,stack)
		stack.insert(0,v)

	def topologicalSort(self):
		visited = [False]*self.V
		stack = []

		for i in range(self.V):
			if visited[i] == False:
				self.topologicalSortUtil(i,visited,stack)

		print(stack)

if __name__ == "__main__":
	g= Graph(6)
	g.addEdge(5, 2)
	g.addEdge(5, 0)
	g.addEdge(4, 0)
	g.addEdge(4, 1)
	g.addEdge(2, 3)
	g.addEdge(3, 1)
	print(g._display())
	print('Build Order/ Topological sort: ')
	g.topologicalSort()

