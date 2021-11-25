import numpy as np 

#a-below, c - main, b - above

def TDMA(diagonalBelow,mainDiagonal,diagonalAbove,solVector):
    n = len(solVector)
    w= np.zeros(n-1,float)
    g= np.zeros(n, float)
    p = np.zeros(n,float)
    
    w[0] = diagonalAbove[0]/mainDiagonal[0]
    g[0] = solVector[0]/mainDiagonal[0]

    for i in range(1,n-1):
        w[i] = diagonalAbove[i]/(mainDiagonal[i] - diagonalBelow[i-1]*w[i-1])
    for i in range(1,n):
        g[i] = (solVector[i] - diagonalBelow[i-1]*g[i-1])/(mainDiagonal[i] - diagonalBelow[i-1]*w[i-1])
    p[n-1] = g[n-1]
    for i in range(n-1,0,-1):
        p[i-1] = g[i-1] - w[i-1]*p[i]
    print("after TDMA x[n]= ")
    print(p)

#a,b
def gssjrdn(m, solVector):
	a = m
	b = solVector
	a = np.array(a,dtype=float)
	b = np.array(b,dtype=float)
	n = len(b)
	print("gssjrdn starting: ")
	print("")
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

def main():
	n = np.random.randint(low=3, high=10)
	diagonalAbove = np.random.rand(n-1)
	mainDiagonal = np.random.rand(n)
	diagonalBelow = np.random.rand(n-1)
	solVector = np.random.rand(n)
	m = np.diag(diagonalAbove, k =1) + np.diag(mainDiagonal, k = 0) + np.diag(diagonalBelow, k=-1)
	TDMA(diagonalBelow, mainDiagonal, diagonalAbove, solVector)
	gssjrdn(m, solVector)


main()