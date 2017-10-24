# Check if a given string is a permutation of a palindrome string
def palindromePermutation(s):
	# remove whitespaces
	s = s.replace(" ", "").lower()
	d = {}
	
	for w in s:
		if w not in d:
			d[w] = 1
		else:
			d[w] += 1

	# odd
	if len(s)%2 != 0:
		flag = False
		for k,v in d.items():	
			if v%2 != 0:
				if flag:
					return False
				flag = True
		return True

	else:
		flag = False
		for k,v in d.items():
			if v%2 != 0:
				return False
		return True 

def main():
	s = "Tact Coa"
	print(palindromePermutation(s))

if __name__ == "__main__":
	main()