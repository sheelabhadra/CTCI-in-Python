# Implement a graph as an Adjacency list
# Using a dictionary

class Vertex:
	def __init__(self,key):
		self.id = key
		self.connectedTo = {}

	def addNeighbor(self,nbr,weight=0):
		self.connectedTo[nbr] = weight

	def getConnections(self):
		self.connectedTo.keys()

	def getId(self):
		return self.id

	def getWeight(self,nbr):
		return self.connectedTo[nbr]

	def __str__(self):
		return str(self.id) + " connected to: " + str([x.id for x in self.connectedTo])

class Graph:
	def __init__(self):
		self.vertList = {}
		self.numVertices = 0

	def addVertex(self,key):
		self.numVertices += 1
		newVertex = Vertex(key)
		self.vertList[key] = newVertex
		return newVertex

	def getVertex(self,n):
		if n in self.vertList:
			return self.vertList[n]
		else:
			return None

	def addEdge(self,f,t,cost=0):
		if f not in self.vertList:
			nv = self.addVertex(f)
		if t not in self.vertList:
			nv = self.addVertex(t)

		self.vertList[f].addNeighbor(self.vertList[t],cost)

	def getVertices(self):
		return self.vertList.keys()

	def __iter__(self):
		return iter(self.vertList.values())

	def __contains__(self,n):
		return n in self.vertList

# create a Graph
g = Graph()
for i in range(6):
	g.addVertex(i)
g.addEdge(0,1,2)

for vertex in g:
	print(vertex)
	print(vertex.getConnections)
	print("\n")






