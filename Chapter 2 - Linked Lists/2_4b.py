# Partition
class Node(object):
	def __init__(self,data):
		self.data = data
		self.next = None

def partition(node, val):
	# Create 2 linked lists - 1 that stores elements < partition value, the other that stores >= partition value
	# Merge the 2 linked lists after traversing through the whole original list

	# Partition
	head, tail = node, node

	while node != None:
		temp = node.next
		if node.data < val:
			# Insert node at head
			node.next = head
			head = node
		else:
			# Insert node at tail
			tail.next = node
			tail = node
		node = temp
	tail.next = None
	return head

def display(node):
	while node != None:
		if node.next != None:
			print(str(node.data), end="->")
		else:
			print(str(node.data), end="")
		node = node.next

def main():
	a = Node(3)
	b = Node(5)
	c = Node(8)
	d = Node(5)
	e = Node(10)
	f = Node(2)
	g = Node(1)

	a.next = b
	b.next = c
	c.next = d
	d.next = e
	e.next = f
	f.next = g

	print("Original list : ")
	display(a)

	print("\nAfter partitioning (around 5) the new list is : ")
	node = partition(a, 5)
	display(node)

if __name__ == "__main__":
	main()
