# URLify
def URLify(s, true_len):
	s = list(s) # convert string to list since string is immutable in Python
	n_spaces = 0
	for i in range(true_len):
		if s[i] == " ":
			n_spaces += 1

	index = true_len + n_spaces*2

	for i in range(true_len-1, -1, -1):
		if s[i] == " ":
			s[index - 1] = "0"
			s[index - 2] = "2"
			s[index - 3] = "%"
			index = index - 3
		else:
			s[index - 1] = s[i]
			index -= 1
	return "".join(s) # convert list back to string

def main():
	s = "Mr John Smith    "
	true_len = 13
	print(URLify(s, true_len))

if __name__ == "__main__":
	main()