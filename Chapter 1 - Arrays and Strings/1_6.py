# String Compression
def stringCompress(s):
	length, i, start = len(s), 0, 1
	compressed = []

	while i < length-1:
		if s[i] != s[i+1]:
			compressed.extend([s[i], str(start)])
			start = 1
			i += 1
		else:
			i += 1
			start += 1
	
	# check the last 2 characters
	if s[i] != s[i-1]:
		compressed.extend([s[i], "1"])
	else:
		compressed.extend([s[i], str(start)])

	if len(compressed) < len(s):
		return ''.join(compressed)
	else:
		return s

def main():
	s = "aabcccccaaab"
	print("Given string: {}, Compressed string: {}".format(s, stringCompress(s)))

	s= "abcbabs"
	print("Given string: {}, Compressed string: {}".format(s, stringCompress(s)))

if __name__ == "__main__":
	main()


