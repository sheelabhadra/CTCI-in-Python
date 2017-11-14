# DFS implementation using a Stack

def dfs(graph, start):
	visited = set()
	stack = [start]

	while stack:
		vertex = stack.pop()

		if vertex not in visited:
			visited.add(vertex)
			stack.extend(graph[vertex] - visited)

	return visited

if __name__ == "__main__":
	graph = {'A': set(['B', 'C']),
			'B': set(['A', 'D', 'E']),
			'C': set(['A', 'F']),
			'D': set(['B']),
			'E': set(['B', 'F']),
			'F': set(['C', 'E'])}
	print(dfs(graph, 'A'))