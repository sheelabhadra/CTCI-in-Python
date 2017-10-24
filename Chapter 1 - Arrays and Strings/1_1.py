# Is Unique
# Using an additional data structure : dictionary
def isUnique(s):
	d = {}
	for e in s:
		if e in d:
			return False
		else:
			d[e] = 1
	return True

def main():
	s = "hello"
	print(s, " : " , isUnique(s))
	s = "world"
	print(s, " : " , isUnique(s))

if __name__ == "__main__":
	main()
