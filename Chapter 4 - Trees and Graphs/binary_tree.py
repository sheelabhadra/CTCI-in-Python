# Binary tree implementation
class BinaryTree(object):
	def __init__(self, root=None):
		self.key = root
		self.left = None
		self.right = None

	def insertLeft(self, newNode):
		if self.left == None:
			self.left = BinaryTree(newNode)
		else:
			# Insert a node and push the existing child down one level in the tree
			t = BinaryTree(newNode)
			t.left = self.left
			self.left = t

	def insertRight(self, newNode):
		if self.right == None:
			self.right = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			t.right = self.right
			self.right = t

	def getLeft(self):
		return self.left

	def getRight(self):
		return self.right

	def setRootVal(self, val):
		self.key = val

	def getRootVal(self):
		return self.key

if __name__ == "__main__":
	root = BinaryTree(10)
	root.insertLeft(5)
	root.insertRight(20)
	root.getLeft().insertRight(12)
	root.getRight().insertLeft(3)
	root.getRight().insertRight(7)
	root.getRight().getLeft().insertLeft(9)
	root.getRight().getLeft().insertRight(18)




