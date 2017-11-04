# Implementation of a Stack using arrays
def createStack():
	stack = []
	return stack

def push(stack, data):
	stack.append(data)

def pop(stack):
	# Check if the stack is Empty
	if isEmpty(stack):
		return "Stack is empty." # minus infinity

	return stack.pop()

def isEmpty(stack):
	return len(stack) == 0

def main():
	s = createStack()
	push(s, 10)
	push(s, 20)
	push(s, 30)
	push(s, 40)
	while not isEmpty(s):
		print(pop(s))
	print(pop(s))

if __name__ == "__main__":
	main()
