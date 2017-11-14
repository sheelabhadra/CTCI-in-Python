# DFS implementation using a Stack

def dfs(graph, start, visited=None):
	if visited is None:
		visited = set()
	visited.add(start)

	for nxt in graph[start] - visited:
		dfs(graph, nxt, visited)

	return visited

if __name__ == "__main__":
	graph = {'A': set(['B', 'C']),
			'B': set(['A', 'D', 'E']),
			'C': set(['A', 'F']),
			'D': set(['B']),
			'E': set(['B', 'F']),
			'F': set(['C', 'E'])}
	print(dfs(graph, 'A'))