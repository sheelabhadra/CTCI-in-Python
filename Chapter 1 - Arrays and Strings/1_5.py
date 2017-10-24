# One Away
def oneReplace(s1,s2):
	flag = False
	for w1,w2 in zip(s1,s2):
		if w1 != w2:
			if flag:
				return False
			flag = True
	return True

def oneInsert(s1,s2):
	# it is assumed that length of s1 is less than lenght of s2
	index1, index2 = 0, 0
	while index1 < len(s1) and index2 < len(s2):
		if s1[index1] != s2[index2]:
			if index1 != index2:
				return False
			index2 += 1
		else:
			index1 += 1
			index2 += 1
	return True

def oneAway(s1,s2):
	if len(s1) == len(s2):
		return oneReplace(s1,s2)

	elif len(s1) + 1 == len(s2):
		return oneInsert(s1,s2)

	elif len(s1) == len(s2) + 1:
		return oneInsert(s2,s1)
	
	else:
		return False

def main():
	s1 = "pale"
	s2 = "plea"
	print("s1 = {} and s2 = {} : {}".format(s1, s2, oneAway(s1,s2)))
	
	s1 = "pales"
	s2 = "pale"
	print("s1 = {} and s2 = {} : {}".format(s1, s2, oneAway(s1,s2)))

	s1 = "pale"
	s2 = "bale"
	print("s1 = {} and s2 = {} : {}".format(s1, s2, oneAway(s1,s2)))

	s1 = "pale"
	s2 = "bake"
	print("s1 = {} and s2 = {} : {}".format(s1, s2, oneAway(s1,s2)))

if __name__ == "__main__":
	main()