from numpy import array, zeros, size, dot
from numpy.linalg import norm, inv

def Jacobiano (F, xp):
    N = size(xp)
    dx = 1e-3
    
    x = zeros(N)
    Jab = zeros([N,N])
    for j in range(N):
        x[j] = dx
        Jab[:,j] = ( F(xp + x ) - F(xp - x) ) /(2*dx)
    return Jab

def LU(A):
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
 
	return L@U

def GAUSS(A,b):
    
    x = zeros(size(b))
    y = zeros(size(b))
    
    A = LU(A)
    y[0] = b[0]
    
    for i in range(size(b) ):
        y[i] = b[i] - dot( A[i,0:i], y[0:i] )
        
    x[size(b)-1] = y[size(b)-1] / A[size(b)-1,size(b)-1]
    
    for i in range(size(b)-2, -1, -1):
        x[i] = ((y[i] - dot(A[i, i+1:size(b)+1], x[i+1:size(b)+1])) / A[i,i])
    
    return x

def Inversa(A):

    B = zeros([size(A,1), size(A,1)])

    for i in range(size(A,1)):
        
        a = zeros(size(A,1))
        a[i] = 1

        B[:,i] = GAUSS(A, a)
    
    return B
        
def Newton(F,x0):
    
    if type(x0) == "numpy.ndarray":
        N = size(x0)
        dx = 2 * x0
        it = 0 #Initialization of iterations
        itmax = 1000 #max iterations
        eps = 1 # initial error
        
        while (eps > 1e-8) and (it <= itmax):
            it = it + 1
            Jab = Jacobiano(F, x0)
            b = F(x0)
            dx = dot( inv(Jab), b)
            x0 = x0 - dx
            eps = norm(dx)
        return x0
    
    else:
        for i in range(1000):
            it = 0
            x1 = x0 - F(x0) / prime(F,x0)
            x0 = x1
            it += 1
        return x0
    
def Newton_LU(F,x0):
    N = size(x0)
    dx = 2 * x0
    it = 0 #Initialization of iterations
    itmax = 1000 #max iterations
    eps = 1 # initial error
    
    while (eps > 1e-8) and (it <= itmax):
        it = it + 1
        dx = dot( Inversa(Jacobiano(F, x0)), F(x0))
        x0 = x0 - dx
        eps = norm(dx)
        
    return x0

def prime(F, x):

    return (F(x + 10e-6) - F(x - 10e-6)) / 20e-6

