def stringRotation(s1, s2):
	s1s1 = s1 + s1
	return isSubstring(s1s1, s2):

def main():
	s1 = "waterbottle"
	s2 = "erbottlewat"
	if stringRotation(s1,s2):
		print("{} is a rotation of {}.".format(s2,s1))

	else:
		print("{} is not a rotation of {}.".format(s2,s1))

if __name__ == "__main__":
	main()