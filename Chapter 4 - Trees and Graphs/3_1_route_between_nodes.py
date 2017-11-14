# Using a DFS
def route_dfs(graph, start, goal):
	stack = [(start, [start])]

	while stack:
		(vertex, path) = stack.pop()
		for nxt in graph[vertex] - set(path):
			if nxt == goal:
				yield path + [nxt]
			else:
				stack.append((nxt, path+[nxt]))


# Using a BFS
def route_bfs(graph, start, goal):
	queue = [(start, [start])]

	while queue:
		(vertex, path) = queue.pop(0)
		for nxt in graph[vertex] - set(path):
			if nxt == goal:
				yield path + [nxt]
			else:
				queue.append((nxt, path+[nxt]))


if __name__ == "__main__":
	# Directed graph
	graph = {'A': set(['B','C']),
		'B': set(['E']),
		'C': set(['F']),
		'D': set(['B']),
		'E': set(['F']),
		'F': set([])}

	start, goal = 'A', 'F'
	
	print("======== Using DFS ========")
	print("The paths between node {} and node {} are ".format(start, goal))
	if len(list(route_dfs(graph, start, goal))) != 0:
		print(list(route_dfs(graph, start, goal)))
	else:
		print("No path!")

	print("\n======== Using BFS ========")
	print("The paths between node {} and node {} are ".format(start, goal))
	if len(list(route_bfs(graph, start, goal))) != 0:
		print(list(route_bfs(graph, start, goal)))
	else:
		print("No path!")


