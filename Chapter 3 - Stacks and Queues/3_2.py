# Stack min
# Time: O(1)
# Space: O(n)
import sys

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

class MinStack:
	#stack2 = Stack()
	def __init__(self):
		self.stack = []
		self.stack2 = Stack()

	def push(self, data):
		if data < self.min():
			# push to new stack
			self.stack2.push(data)
		self.stack.append(data)

	def isEmpty(self):
		return len(self.stack) == 0 

	def pop(self):
		if self.isEmpty():
			return "Stack is empty."
		data = self.stack.pop()
		if data == self.min():
			self.stack2.pop()	
		return data

	def peek(self):
		return self.stack[len(self.stack)-1]

	def min(self):
		if self.stack2.isEmpty():
			return sys.maxsize
		else:
			return self.stack2.peek()

def main():
	s = MinStack()
	s.push(10)
	s.push(20)
	s.push(30)
	print("The minimum element is : ", s.min())
	
	print(s.pop())
	s.push(50)
	print("The element at the top is: ",s.peek())
	s.push(5)
	print("The minimum element is : ", s.min())

if __name__ == "__main__":
	main()