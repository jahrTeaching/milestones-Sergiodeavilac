from numpy import array, zeros, size, dot
from numpy.linalg import norm, inv
# from ODES.Jab_Newt import solve_LU as SL
from ODES.Jab_Newt import LU, Inversa


A = array([[1, 2, 3],[4,5, 6],[7, 8, 9]])


def factorization_LU(A):

	N = size(A,1)
	U = zeros([N,N])
	L = zeros([N,N])

	U[0,:] = A[0,:]
	for k in range(0,N):
		L[k,k] = 1

	L[1:N,0] = A[1:N,0]/U[0,0]


	for k in range(1,N):

		for j in range(k,N):
			U[k,j] = A[k,j] - dot(L[k,0:k], U[0:k,j])

		for i in range(k+1,N):
			L[i,k] =(A[i,k] - dot(U[0:k,k], L[i,0:k])) / (U[k,k])

	return [L@U, L, U]


def solve_LU(M,b):

    N=size(b)
    y=zeros(N)
    x=zeros(N)

    [A,L,U] = factorization_LU(M)
    
    y[0] = b[0]

    for i in range(0,N):
        y[i] = b[i] - dot(A[i,0:i], y[0:i])


    x[N-1] = y[N-1]/A[N-1,N-1]

    for i in range(N-2,-1,-1):
        x[i] = (y[i] - dot(A[i, i+1:N+1], x[i+1:N+1])) / A[i,i]

    return x

def Inverse(A):
    
    N = size(A,1)

    B = zeros([N,N])

    for i in range(0,N):
        one = zeros(N)
        one[i] = 1

        B[:,i] = solve_LU(A, one)

    return B
# print(SL(A,b))
print('\n')
print(Inversa(A))
print(Inverse(A))
print(Inversa(A)-Inverse(A))