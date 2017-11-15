# Check if a binary tree is balanced
# Balanced tree: Heights of the 2 subtrees of any node never differ by more than one
class Node:
	def __init__(self, key=None):
		self.val = key
		self.left = None
		self.right = None

def height(node):
	if node == None:
		return 0 # Base case

	return 1 + max(height(node.left), height(node.right))

# This method is not efficient since at each node we recurse through its entire subtree
# So we find height repeatedly at the same nodes 
# Time: O(NlogN) since each node is touched once per node above it
def checkBalanced(node):
	if node == None:
		return True

	lh = height(node.left) # Height of left sub tree
	rh = height(node.right) # Height of right sub tree

	if abs(lh-rh) > 1:
		return False
	else:
		return (checkBalanced(node.left) and checkBalanced(node.right))

if __name__ == "__main__":
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)
	root.right.left = Node(6)
	root.right.left.right = Node(7)
	#root.right.left.right = Node(8)
	print(checkBalanced(root))



