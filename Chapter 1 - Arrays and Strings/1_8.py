# zero matrix
def zeroMatrix(M):
	rowHasZero = [False]*len(M)
	colHasZero = [False]*len(M[0])

	# Check positions where there are 0s in the matrix
	for i in range(len(M)):
		for j in range(len(M[0])):
			if M[i][j] == 0:
				rowHasZero[i] = True
				colHasZero[j] = True

	# Nullify rows
	for i in range(len(M)):
		if rowHasZero[i]:
			for j in range(len(M[0])):
				M[i][j] = 0

	# Nullify columns
	for j in range(len(M[0])):
		if colHasZero[j]:
			for i in range(len(M)):
				M[i][j] = 0
	return M

def zeroMatrixOpt(M):
	rowHasZero = False
	colHasZero = False

	# Check if there is a 0 in the 1st row
	for i in range(len(M)):
		if M[i][0] == 0:
			rowHasZero = True
			break

	# Check if there is a 0 in the 1st column		
	for j in range(len(M[0])):
		if M[0][j] == 0:
			colHasZero = True
			break

	# Check in the remaining matrix
	for i in range(1, len(M)):
		for j in range(1, len(M[0])):
			if M[i][j] == 0:
				M[i][0] = 0
				M[0][j] = 0

	for i in range(1, len(M)):
		if M[i][0] == 0:
			for j in range(1, len(M[0])):
				M[i][j] = 0

	for j in range(1, len(M[0])):
		if M[0][j] == 0:
			for i in range(1, len(M)):
				M[i][j] = 0

	if rowHasZero:
		for i in range(len(M)):
			M[i][0] = 0

	if colHasZero:
		for j in range(len(M[0])):
			M[0][j] = 0
	return M

def main():
	M = [[1,2,0,6],
		 [3,0,3,2],
		 [4,1,6,3],
		 [5,7,0,4]]
	
	#print("The nullified matrix is ", zeroMatrix(M))

	print("The nullified matrix is", zeroMatrixOpt(M))

if __name__ == "__main__":
	main()