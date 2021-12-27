import numpy as np
np.set_printoptions(linewidth=100, precision=5,suppress=True)



def main(A):
	
	A = np.array(A, float)
	B = np.zeros_like(A, float)
	T = np.zeros_like(A, float)
	y = np.zeros_like(A, float)
	x = np.zeros_like(A, float)
	o = np.zeros_like(A, float)
	n = len(A)

	for i in range(n):
		B[i,0] = A[i,0]
	for j in range(n):
		T[0,j] = A[0,j]/B[0,0]
	for k in range(1,n): #did a correction
		for i in range(k,n):
			B[i,k] = A[i,k]
			for m in range(k):
				B[i,k] = B[i,k] - B[i,m] * T[m,k]
		if k <= n-1:
			for j in range(k,n):
				T[k,j] = A[k,j]
				for m in range(k):
					T[k,j] = T[k,j] - B[k,m] * T[m,j]
				T[k,j] = T[k,j] / B[k,k]

	for i in range(n):
		for j in range(n):
			if j > i:
				y[i,j] = 0
			elif j == i:
				y[i,j] = 1 / B[i,i]
			elif j < i:
				for m in range(j, i):
					y[i,j] = y[i,j] - B[i,m] * y[m,j]
				y[i,j] = y[i,j] / B[i,i]

	for i in range(n-1, -1, -1):
		for j in range(n-1,-1,-1):
			if j < i:
				x[i,j] = 0
			elif j == i:
				x[i,j] = 1
			elif j > i:

				for m in range(i+1, j+1):
					x[i,j] = x[i,j] - T[i,m] * x[m,j]

	

	print(f"B:\n{B}")
	print(f"T:\n{T}")
	print(f"Y:\n{y}")
	print(f"X:\n{x}")
	print("")
	print(np.matmul(x,y))
	print("Для проверки")
	print(np.linalg.inv(A))

A = [[8,1,2,1,4,9],
	 [9,7,7,3,4,3],
	 [4,3,9,7,2,9],
	 [5,4,7,3,8,4],
	 [3,6,4,4,5,3],
	 [9,2,8,3,6,9]]

main(A)


