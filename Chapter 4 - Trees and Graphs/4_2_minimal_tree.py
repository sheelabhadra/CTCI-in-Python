# Given a sorted array of unique integer elements,
# write an algorithm to create a BST with minimal height

#STEPS:
#1. Get the Middle of the array and make it root.
#2. Recursively do same for left half and right half.
#   a) Get the middle of left half and make it left child of the root
#      created in step 1.
#   b) Get the middle of right half and make it right child of the
#      root created in step 1.

class Node:
	def __init__(self, key):
		self.val = key
		self.left = None
		self.right = None

def minimalTree(arr, start, end):
	if end < start:
		return None

	mid = (start + end)//2
	n = Node(arr[mid])

	n.left = minimalTree(arr, start, mid-1)
	n.right = minimalTree(arr, mid+1, end)
	return n

def preOrder(node):
	if node == None:
		return
	print(str(node.val) + " ")
	preOrder(node.left)
	preOrder(node.right)

if __name__ == "__main__":
	arr = [1,2,3,4,5,6,7]
	root = minimalTree(arr, 0, len(arr)-1)
	print("The preorder traversal of the constructed BST: ")
	preOrder(root)
