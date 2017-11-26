# Check Subtree: T1 and T2 are two very large binary trees, with T1 much bigger than T2. Create an
# algorithm to determine if T2 is a subtree of T1.
# A tree T2 is a subtree of T1 if there exists a node n in T1 such that the subtree of n is identical to T2.
# That is, if you cut off the tree at node n, the two trees would be identical.

# SOLUTION: Do pre-order traversal on both the trees, T1 and T2
# Replace each `None` node by a marker e.g. `X`
# If T1 is a subtree of T2 then the pre-order traversal of T2 will be a substring of T1

class Node:
	def __init__(self, data=None):
		self.data = data
		self.left = None
		self.right = None

def getOrder(node, s):
	if node == None:
		s = s + 'X'
		return
	s = s + str(node.data) # Add root
	getOrder(node.left, s) # Add left node
	getOrder(node.right, s) # Add right node

def containsTree(t1, t2):
	s1 = ''
	s2 = ''

	getOrder(t1, s1)
	getOrder(t2, s2)

	# Check if s2 is a substring of s1
	return s2 in s1

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




