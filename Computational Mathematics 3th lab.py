import numpy as np

def gssjrdn(a,b):

	a = np.array(a,dtype=float)
	b = np.array(b,dtype=float)
	n = len(b)

	#main loop 
	for k in range(n):
		#partial pivoting
		if np.fabs(a[k,k]) < 1.0e-12:
			for i in range(k+1,n):
				if np.fabs(a[i,k]) > np.fabs(a[k,k]):
					for j in range(k,n):
						a[k,j],a[i,j] = a[i,j],a[k,j]
					b[k],b[i] = b[i],b[k]
					break
		#Division of the pivot row
		pivot = a[k,k]
		for j in range(k,n):
			a[k,j] /= pivot
		b[k] /= pivot
		#Elimiination loop
		for i in range(n):
			if i == k or a[i,k] == 0:continue
			factor = a[i,k]
			for j in range(k,n):
				a[i,j] -= factor * a[k,j]
			b[i] -= factor * b[k]
			print(a,b)
			print("")
	return b,a

a = [[0.18,0.34,0.31,0.19,-0.43],
	[-0.53,-0.8,0.05,-0.29,0.73],
	[0.48,0.44,-0.36,-0.64,0.17],
	[0.62,-0.42,0.22,-0.8,0.77],
	[-0.21,0.96,0.93,-0.87,0.77]]
b = [-0.31,-0.48,-0.56,0.08,-0.03]

gssjrdn(a,b)
