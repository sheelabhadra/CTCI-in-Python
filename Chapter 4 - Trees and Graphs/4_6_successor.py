# In-order Successor
#Successor: Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a
#binary search tree. You may assume that each node has a link to its parent.

class Node:
	def __init__(self, key=None):
		self.data = key
		self.left = None
		self.right = None

"""
def leftMostChild(n):
	if n == None:
		return None
	while n.left != None:
		n = n.left
	return n


def inOrderSuccessor(n):
    if n == None:
    	return None

    if n.right != None:
    	return leftMostChild(n.right)
    else:
    	q = n
    	x = q.parent
    	while x != None and x.left != q:
    		q = x
    		x = x.parent
    	return x

    
if __name__ == "__main__":
	root = Node(20)
	root.left = Node(8)
	root.left.left = Node(4)
	root.left.right = Node(12)
	root.left.right.left = Node(10)
	root.left.right.right = Node(14)
	root.right = Node(22)
	temp = root.left.right.right
	succ = inOrderSuccessor(temp)
	if succ is not None:
	    print("Inorder Successor of %d is %d "%(temp.data , succ.data))
	else:
	    print("\nInorder Successor doesn't exist")
"""
def inOrderSuccessor(root, n):
     
    # Step 1 of the above algorithm
    if n.right is not None:
        return minValue(n.right)
 
    # Step 2 of the above algorithm
    p = n.parent
    while( p is not None):
        if n != p.right :
            break
        n = p 
        p = p.parent
    return p
 
# Given a non-empty binary search tree, return the 
# minimum data value found in that tree. Note that the
# entire tree doesn't need to be searched
def minValue(node):
    current = node
 
    # loop down to find the leftmost leaf
    while(current is not None):
        if current.left is None:
            break
        current = current.data
 
    return current
 
 
# Given a binary search tree and a number, inserts a
# new node with the given number in the correct place
# in the tree. Returns the new root pointer which the
# caller should then use( the standard trick to avoid 
# using reference parameters)
def insert( node, data):
 
    # 1) If tree is empty then return a new singly node
    if node is None:
        return Node(data)
    else:
        
        # 2) Otherwise, recur down the tree
        if data <= node.data:
            temp = insert(node.left, data)
            node.left = temp 
            temp.parent = node
        else:
            temp = insert(node.right, data)
            node.right = temp 
            temp.parent = node
         
        # return  the unchanged node pointer
        return node
 
 
# Driver progam to test above function
 
root  = None

root = insert(root, 20)
root = insert(root, 8);
root = insert(root, 22);
root = insert(root, 4);
root = insert(root, 12);
root = insert(root, 10);  
root = insert(root, 14);    
temp = root.left.right.right 
# root = Node(20)
# root.left = Node(8)
# root.left.left = Node(4)
# root.left.right = Node(12)
# root.left.right.left = Node(10)
# root.left.right.right = Node(14)
# root.right = Node(22)
# temp = root.left.right.right
 
succ = inOrderSuccessor( root, temp)
if succ is not None:
    print("\nInorder Successor of %d is %d "%(temp.data , succ.data))
else:
    print("\nInorder Successor doesn't exist")