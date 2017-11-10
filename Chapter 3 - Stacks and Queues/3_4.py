# Queue using 2 stacks
class Stack:
	def __init__(self):
		self.stack = []

	def push(self, data):
		self.stack.append(data)

	def isEmpty(self):
		return len(self.stack) == 0 

	def pop(self):
		if self.isEmpty():
			return "Stack is empty."
		return self.stack.pop()

	def peek(self):
		return self.stack[len(self.stack)-1]

	def size(self):
		return len(self.stack)

	def index(self, i):
		return self.stack[i]


class MyQueue:
	def __init__(self):
		self.stack1 = Stack()
		self.stack2 = Stack()

	def add(self, data):
		self.stack1.push(data)

	# Step 1. Pop everything from stack 1 to stack 2
	# Step 2. Push everything back to stack 1 after the pop()/peek() operation
	def remove(self):
		while not self.stack1.isEmpty():
			self.stack2.push(self.stack1.pop())
		popped = self.stack2.pop()

		while not self.stack2.isEmpty():
			self.stack1.push(self.stack2.pop())
		return popped

	def isEmpty(self):
		return self.stack1.size() == 0

	# Same approach as pop()
	def peek(self):
		while not self.stack1.isEmpty():
			self.stack2.push(self.stack1.pop())
		popped = self.stack2.index(self.stack2.size()-1)

		while not self.stack2.isEmpty():
			self.stack1.push(self.stack2.pop())
		return popped

def main():
	queue = MyQueue()
	seq = ['1','2','3','4', '5']
	for item in seq:
		queue.add(item)
	print("The top most item in the queue is {}.".format(queue.peek()))

	print("Removing the items from the queue: ")
	while not queue.isEmpty():
		print(queue.remove())

if __name__ =="__main__":
	main()
