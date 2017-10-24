# Rotate Matrix
def rotateMat(M,dir):
	N = len(M)
	# ======= Without allocating extra space === #
	# Step 1: Find the transpose of the matrix
	for i in range(N):
		for j in range(i,N):
			if i != j:
				# swap
				M[j][i], M[i][j] = M[i][j], M[j][i]
	print("The transposed matrix is ", M)
	# Step 2: If the rotation = +90 (Clockwise) => rotate about center laterally
	#         If the rotation = -90 (Anti-clockwise) => rotate about center vertically
	if dir == "-90":
		for i in range(N//2):
			for j in range(N):
				# swap
				M[i][j], M[N-1-i][j] = M[N-1-i][j], M[i][j]
		return M

	else:
		for i in range(N):
			for j in range(N//2):
				# swap
				M[i][j], M[i][N-1-j] = M[i][N-1-j], M[i][j]
		return M



	"""
	# ======== Allocating extra space ========= #
	res = [[0]*N for row in range(N)]
	if dir == "-90":
		for i in range(N):
			for j in range(N):
				res[i][j] = M[j][N-1-i]
		return res
	
	else:
	 	for i in range(N):
	 		for j in range(N):
	 			res[i][j] = M[N-1-j][i]
	 	return res
	# ========================================== #
	"""

def main():
	M = [[1,2,3,4],
		 [5,6,7,8],
		 [9, 10, 11, 12],
		 [13, 14, 15, 16]]
	print("The original matrix is ", M)
	dir = "-90"
	print("The anti-clockwise rotated matrix is {}".format(rotateMat(M, dir)))
	dir = "+90"
	print("The clockwise rotated matrix is {}".format(rotateMat(M, dir)))

if __name__ == "__main__":
	main()