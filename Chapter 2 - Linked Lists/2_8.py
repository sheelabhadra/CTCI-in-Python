# Loop Detection
# STEPS
#1. Create two pointers, FastPointer and SlowPointer.
#2. Move FastPointer at a rate of 2 steps and SlowPointer at a rate of 1 step.
#3. When they collide, move SlowPointer to LinkedListHead. Move FastPointer to the next node (1 step) where it is.
#4. Move SlowPointer and FastPointer at a rate of one step. Return the new collision point.

class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None

def getSize(node):
	count = 1
	while node.next != None:
		count += 1
		node = node.next
	return count, node

def findLoopStart(slow, fast):
	pos = 1
	while slow != fast:
		slow = slow.next
		fast = fast.next
		pos += 1
	return slow, pos

def checkLoop(node):
	slow, fast = node, node.next
	while fast != None and fast.next != None:
		print(slow.data, fast.data)
		if slow == fast:
			break
		slow = slow.next
		fast = fast.next.next
	if slow == fast:
		slow = node
		fast = fast.next
		return findLoopStart(slow, fast)
	return None

def display(node):
	while node != None:
		if node.next != None:
			print(str(node.data), end=" -> ")
		else:
			print(str(node.data), end="")
		node = node.next

def main():
	a = Node(3)
	b = Node(1)
	c = Node(5)
	d = Node(9)
	e = Node(7)
	f = Node(2)
	g = Node(1)

	a.next = b
	b.next = c
	c.next = d
	d.next = e
	e.next = f
	f.next = g
	g.next = c

	print("The list is : a -> b -> c -> d -> e -> f -> g -> c .")
	if checkLoop(a):
		print("The loop starts at position {} from the start of the list.".format(checkLoop(a)[1]))
	else:
		print("There is no loop in the list.")
	

if __name__ == "__main__":
	main()