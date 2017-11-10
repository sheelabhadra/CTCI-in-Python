# Sort Stack
# using only 1 extra temporary stack

# STEPS:
# 1. If the top most element of the stack > top most element of the stack2, pop the element and push to stack2	
# 2. Else find the position where the element should enter in stack2 in a counter
# 3. Pop the elements till count from stack2 to stack and push the previously popped element to stack2
# 4. Pop all elemnents from stack2 to stack

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


def sortStack(s):
	s2 = Stack() # create a temporary stack for sorting

	while not s.isEmpty():
		temp = s.pop()
		while not s2.isEmpty() and s2.peek() > temp:
			s.push(s2.pop()) # pop from stack2 and push to stack till s2.peek() > the popped element
		s2.push(temp)

	while not s2.isEmpty():
		s.push(s2.pop()) 

	return s


def main():
	s = Stack()
	seq = ['2', '5', '1', '3', '1']

	for item in seq:
		s.push(item)

	s = sortStack(s)

	print("The popped elements in sorted order: ")
	while not s.isEmpty():
		print(s.pop())

if __name__ == "__main__":
	main()


