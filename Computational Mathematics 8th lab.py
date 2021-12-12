import numpy as np

def main(A):
	n = len(A)
	A = np.array(A, float)
	E = np.zeros_like(A, float)
	np.fill_diagonal(E, 1, float)
	B = np.hstack((A,E))

	for nrow in range(n):
		pivot = nrow + np.argmax(np.fabs(B[nrow:, nrow]))
		# np.argmax возвращает номер строки с максимальным элементом в уменьшенной матрице
		if pivot != nrow:
			B[[nrow, pivot]] = B[[pivot, nrow]]
		row = B[nrow]
		divider = row[nrow]
		if np.fabs(divider) < 1e-10:
			raise ValueError(f"матрица не подходит")
		row /= divider
		for lower_row in B[nrow+1:]:
			factor = lower_row[nrow]
			lower_row -= factor*row

	for nrow in range(n-1,0,-1):
		row = B[nrow]
		for upper_row in B[:nrow]:
			factor = upper_row[nrow]
			upper_row -= factor*row
	print(B)

			
A = [[4,9,4,4],
	 [5,7,6,8],
	 [5,1,6,7],
	 [8,4,7,2]]

main(A)