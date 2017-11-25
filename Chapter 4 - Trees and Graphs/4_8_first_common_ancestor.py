# First Common Ancestor: Design an algorithm and write code to find the first common ancestor
# of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not
# necessarily a binary search tree.
class Node:
	def __init__(self, key=None):
		self.data = key
		self.left = None
		self.right = None


def covers(root, p):
	if root == None:
		return False
	if root == p:
		return True
	return covers(root.left, p) or covers(root.right, p)


def ancestorHelper(root, p, q):
	if root == None or p == None or q == None:
		return root
	pIsOnLeft = covers(root.left,p)
	qIsOnLeft = covers(root.left,q)
	if pIsOnLeft != qIsOnLeft:
		return root

	if pIsOnLeft:
		childide = root.left
	else:
		childside = root.right
	return ancestorHelper(childide, p, q)


def commonAncestor(root , p, q):
	# Error check - One node is not in the tree
	if not covers(root,p) or not covers(root,q):
		return None
	return ancestorHelper(root, p, q)


if __name__ == "__main__":
	tree = Node(20)
	tree.left = Node(10)
	tree.right = Node(30)
	tree.left.left = Node(5)
	tree.left.right = Node(15)
	tree.left.left.left = Node(3)
	tree.left.left.right = Node(7)
	tree.left.right.right = Node(17)
	print("First Common Ancestor of {} and {} is : ".format(tree.left.left.right.data, tree.left.right.right.data))
	print(commonAncestor(tree, tree.left.left.right, tree.left.right.right).data)