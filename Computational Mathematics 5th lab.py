import numpy as np


def main(A,C):
	
	A = np.array(A, dtype=float)
	C = np.array(C, dtype=float)
	B = np.zeros_like(A, dtype=float)
	T = np.zeros_like(A, dtype=float)
	Y = np.zeros_like(C, dtype=float)
	X = np.zeros_like(C, dtype=float)
	n = len(C)

	for i in range(n):
		B[i,0] = A[i,0]
	for j in range(1,n):
		T[0,j] = A[0,j]/B[0,0]
	for k in range(1,n): #did a correction
		for i in range(k,n):
			B[i,k] = A[i,k]
			for m in range(k):
				B[i,k] = B[i,k] - B[i,m] * T[m,k]
		if k <= n-2:
			for j in range(k+1,n):
				T[k,j] = A[k,j]
				for m in range(k):
					T[k,j] = T[k,j] - B[k,m] * T[m,j]
				T[k,j] = T[k,j] / B[k,k]

	Y[0] = C[0] / B[0,0]
	for i in range(n):
		Y[i] = C[i]
		for m in range(i):
			Y[i] = Y[i] - B[i,m] * Y[m]
		Y[i] = Y[i] / B[i,i]

	X[n-1] = Y[n-1]
	for i in range(n-2,-1,-1):
		X[i] = Y[i]
		for m in range(i+1,n):

			X[i] = X[i] - T[i,m] * X[m]

	print(f"B:\n{B}")
	print(f"T:\n{T}")
	print(f"Y:\n{Y}")
	print(f"X:\n{X}")


A = [[0.18,0.34,0.31,0.19,-0.43],
	[-0.53,-0.8,0.05,-0.29,0.73],
	[0.48,0.44,-0.36,-0.64,0.17],
	[0.62,-0.42,0.22,-0.8,0.77],
	[-0.21,0.96,0.93,-0.87,0.77]]
C = [-0.31,-0.48,-0.56,0.08,-0.03]

main(A,C)


