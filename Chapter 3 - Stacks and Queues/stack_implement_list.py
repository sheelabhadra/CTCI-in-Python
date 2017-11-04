# Stack implementation using a linked list
class Node(object):
	# Constructor to initialize a node
	def __init__(self, data):
		self.data = data
		self.next = None

class Stack:
	# Constructor to initialize the root of the list
	def __init__(self):
		self.root = None

	def isEmpty(self):
		return True if self.root == None else False

	def push(self, data):
		new = Node(data)
		new.next = self.root
		self.root = new
		print("{} pushed to stack.".format(data))

	def pop(self):
		if self.isEmpty():
			return "The stack is empty."
		temp = self.root
		self.root = self.root.next
		popped = temp.data
		return popped

	def peek(self):
		if self.isEmpty():
			return "The stack is empty."
		return self.root.data

def main():
	s = Stack()
	s.push(10)
	s.push(20)
	s.push(30)
	s.peek()

	while not s.isEmpty():
		print("The popped item is {}.".format(s.pop()))

	print(s.isEmpty())

if __name__ == "__main__":
	main()
