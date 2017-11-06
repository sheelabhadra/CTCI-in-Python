# Stack Class implementation using an array
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

def main():
	s = Stack()
	s.push(10)
	s.push(20)
	s.push(30)
	
	while not s.isEmpty(): 
		print(s.pop())
	
	print(s.pop())

if __name__ == "__main__":
	main()
