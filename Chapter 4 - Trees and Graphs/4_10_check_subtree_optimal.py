# Check Subtree: T1 and T2 are two very large binary trees, with T1 much bigger than T2. Create an
# algorithm to determine if T2 is a subtree of T1.
# A tree T2 is a subtree of T1 if there exists a node n in T1 such that the subtree of n is identical to T2.
# That is, if you cut off the tree at node n, the two trees would be identical.

# SOLUTION: Search for the root node of T2 in T1
# If there's a match then check if T2 and the subtree are identical
# Break from the matching process the moment we find a mismatch

class Node:
	def __init__(self, data=None):
		self.data = data
		self.left = None
		self.right = None


def matchTree(node1, node2):
	if node1 == None and node2 == None:
		return True
	elif node1 == None or node2 == None:
		return False
	elif node1.data != node2.data:
		return False
	else:
		return matchTree(node1.left, node2.left) and matchTree(node1.right, node2.right)


def containsTree(t1, t2):
	if t1 == None:
		return False
	elif t1.data  == t2.data and matchTree(t1, t2):
		return True
	return containsTree(t1.left, t2) or containsTree(t1.right, t2)


if __name__ == "__main__":
	# T1
	root1 = Node(1)
	root1.left = Node(2)
	root1.right = Node(3)
	root1.left.left = Node(4)
	root1.left.right = Node(5)
	root1.right.right = Node(6)
	root1.left.left.right = Node(7)

	# T2
	root2 = Node(2)
	root2.left = Node(4)
	root2.right = Node(5)
	root2.left.right = Node(7)

	print("T2 is a subtree of T1") if containsTree(root1, root2) else print("T2 is not a subtree of T1")




