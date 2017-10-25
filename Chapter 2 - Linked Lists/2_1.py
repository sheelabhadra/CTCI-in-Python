# Remove dups: Write code to remove deuplicates from n unsorted linked list
class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None

# O(N) space, O(N) time
def removeDups(node):
	S = set()
	prev = Node(None)

	while node != None:
		if node.data in S:
			prev.next = node.next
		else:
			S.add(node.data)
			print(node.data)
			prev = node
		node = node.next

def main():
	a = Node(2)
	b = Node(1)
	c = Node(2)
	d = Node(3)
	e = Node(1)
	f = Node(3)
	g = Node(2) 

	a.next = b
	b.next = c
	c.next = d
	d.next = e
	e.next = f
	f.next = g

	removeDups(a)

if __name__ == "__main__":
	main()
