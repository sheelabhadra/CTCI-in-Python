# Check if a binary tree is balanced
# Balanced tree: Heights of the 2 subtrees of any node never differ by more than one
# This method is efficient because it finds the height and checks balance at the same time
# Time: O(N), Space: O(H)

import sys

class Node:
	def __init__(self, key=None):
		self.val = key
		self.left = None
		self.right = None

def height(node):
	if node == None:
		return 0 # Null tree

	lh = height(node.left)
	if lh == -sys.maxsize+1:
		return -sys.maxsize+1

	rh = height(node.right)
	if rh == -sys.maxsize+1:
		return -sys.maxsize+1

	if abs(lh-rh) > 1:
		return -sys.maxsize+1
	else:
		return max(lh,rh) + 1

	return 1 + max(height(node.left), height(node.right))


def checkBalanced(node):
	
	return height(node) != -sys.maxsize+1

if __name__ == "__main__":
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)
	root.right.left = Node(6)
	root.right.left.right = Node(7)
	
	print(checkBalanced(root))



