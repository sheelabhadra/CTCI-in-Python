# Sum Lists
class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None

def sumLists(node1, node2):
	carry = 0
	temp = Node(None)
	result = temp
	while node1 != None or node2 != None or carry > 0:
		sumLL = carry
		if node1 != None:
			sumLL += node1.data
			node1 = node1.next
		if node2 != None:
			sumLL += node2.data
			node2 = node2.next
		result.next = Node(sumLL%10)
		carry = sumLL//10
		result = result.next
	return temp.next

def display(node):
	while node != None:
		if node.next != None:
			print(str(node.data), end="->")
		else:
			print(str(node.data), end="")
		node = node.next

def main():
	a = Node(7)
	b = Node(1)
	c = Node(6)
	
	d = Node(5)
	e = Node(9)
	f = Node(2)

	a.next = b
	b.next = c
	
	d.next = e
	e.next = f

	print("The first list is : ")
	display(a)
	print("\nThe second list is : ")
	display(d)

	# sum is 617 + 295 = 912 (2 -> 1 -> 9)
	s = sumLists(a, d)
	print("\nThe list of the sum is : ")
	display(s)

if __name__ == "__main__":
	main()