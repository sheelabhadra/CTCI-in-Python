# Check permutation

def checkPermutation(s1,s2):
	d = {}
	for w in s1:
		if w in d:
			d[w] += 1
		else:
			d[w] = 1
	for w in s2:
		if w in d:
			d[w] -= 1
		else:
			return False
	for k,v in d.items():
		if v != 0:
			return False
	return True

def main():
	s1 = "able"
	s2 = "elba"
	print("Are s1 = {} and  s2 = {} permutations? : {}".format(s1,s2,checkPermutation(s1,s2)))

	s1 = "was"
	s2 = "sa"
	print("Are s1 = {} and  s2 = {} permutations? : {}".format(s1,s2,checkPermutation(s1,s2)))

if __name__ == "__main__":
	main()