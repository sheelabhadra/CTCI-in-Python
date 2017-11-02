# Find Intersection
# STEPS
# 1. Iterate through both the lists and check their last node. Also get their lengths.

# 2a. If the last nodes are same then the 2 lists definitely intersect at some node.
# 2b. If the last nodes are not same then the 2 lists do not intersect.

# 3. If the lengths of the 2 lists are not same then find the difference between the lengths of the 2 lists.

# 4. Set 2 pointers to the start of each list.    

# 5. On the longer list, advance its pointer by the diffrence of its lengths.

# 6. Traverse on each list until the pointers are same.

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

def findIntersection(node1, node2, diff):
	while diff > 0:
		node1 = node1.next
		diff -= 1
	pos = 1
	while node1 != node2:
		node1 = node1.next
		node2 = node2.next
		pos += 1
	return node1, pos

def checkIntersection(node1, node2):
	if node1 == None or node2 == None:
		return None

	
	l1, l2 = getSize(node1)[0], getSize(node2)[0]

	
	diff = l1 - l2

	if getSize(node1)[1] == getSize(node2)[1]:
		if diff > 0:
			return findIntersection(node1, node2, abs(diff))
		else:
			return findIntersection(node2, node1,abs(diff))
	else:
		return None
	
def display(node):
	while node != None:
		if node.next != None:
			print(str(node.data), end="->")
		else:
			print(str(node.data), end="")
		node = node.next

def main():
	# Case 1: There's an intersection
	a = Node(3)
	b = Node(1)
	c = Node(5)
	d = Node(9)
	e = Node(7)
	f = Node(2)
	g = Node(1)

	h = Node(4)
	i = Node(6)

	a.next = b
	b.next = c
	c.next = d
	d.next = e
	e.next = f
	f.next = g

	h.next = i
	i.next = e

	print("The first list is : ")
	display(a)
	print("\nThe second list is : ")
	display(h)

	if checkIntersection(a, h):
		print("\nThe node of intersection is at position {} from the start of the smaller list.".format(checkIntersection(a, h)[1]))
	else:
		print("\nThe lists do not intersect.")
	
	## =============================================================================== ##
	# Case 2: There's no intersection
	a1 = Node(3)
	b1 = Node(1)
	c1 = Node(5)
	d1 = Node(9)
	e1 = Node(7)
	f1 = Node(2)
	g1  = Node(1)

	a1.next = b1
	b1.next = c1
	c1.next = d1
	d1.next = e1
	e1.next = f1
	f1.next = g1

	a2 = Node(4)
	b2 = Node(6)
	c2 = Node(7)
	d2 = Node(2)
	e2 = Node(1)

	a2.next = b2
	b2.next = c2
	c2.next = d2
	d2.next = e2

	print("The first list is : ")
	display(a1)
	print("\nThe second list is : ")
	display(a2)

	if checkIntersection(a1, a2):
		print("\nThe node of intersection is at position {} from the start of the smaller list.".format(checkIntersection(a1, a2)[1]))
	else:
		print("\nThe lists do not intersect.")

if __name__ == "__main__":
	main()