# return Kth to last node
class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None

def KtoLast(node, K):
	slow, fast = node, node

	for i in range(K):
		if fast != None:
			fast = fast.next
		else:
			return "K is greater than the size of the list"

	while fast != None:
		fast = fast.next
		slow = slow.next

	return slow.data 

def main():
	a = Node(1)
	b = Node(2)
	c = Node(3)
	d = Node(4)
	e = Node(5)
	f = Node(6)
	g = Node(7) 

	a.next = b
	b.next = c
	c.next = d
	d.next = e
	e.next = f
	f.next = g

	print("For K = {}, the data in the node is {}.".format(3, KtoLast(a,3)))
	print("For K = {}, the data in the node is {}.".format(5, KtoLast(a,5)))
	print("For K = {}, {}.".format(8, KtoLast(a,8)))

if __name__ == "__main__":
	main()
