# Validate BST
# Using recursion
# 2 steps - 
# checking that each subtree is valid BST is not sufficient
# the condition is that all left nodes must be less than or equal to the current node, which
# must be less than all the right nodes.
# Using this thought, we can approach the problem by passing down the min and max values. As we iterate
# through the tree, we verify against progressively narrower ranges.
class Node:
	def __init__(self,key=None):
		self.val = key
		self.left = None
		self.right = None


def validBST(node, mini, maxi):
	if node == None:
		return True

	if node.val <= mini or node.val > maxi:
		return False
	
	if not validBST(node.left, mini, node.val) and not validBST(node.right, node.val, maxi):
		return False

	return True


if __name__ == "__main__":
	root = Node(20)
	root.left = Node(10)
	root.left.right = Node(25)
	root.right = Node(30)
	if validBST(root, float("-inf"), float("inf")):
		print("Is a BST")
	else:
		print("Not a BST")