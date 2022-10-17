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
    A[1:N,0] = A[1:N,1] / A[0,0]
    
    for k in range (1,N):
        for j in range(k,N):
            A[k,j] = A[k,j] - dot( A[k, 1:k-1], A[1:k-1, j] )
            
    for i in range(k+1,N):
         A[i,k] =(A[i,k] - dot(A[0:k,k], A[i,0:k])) / (A[k,k])
         
    return A

def solve_LU(A,b):
    
    x = zeros(size(b))
    y = zeros(size(b))
    
    A = LU(A)
    y[0] = b[0]
    
    for i in range(1, size(b) ):
        y[i] = b[i] - dot( A[i,0:i], y[0:i] )
        
    x[-1] = y[-1] / A[-1,-1]
    
    for i in range(-1, 1, -1):
        x[i] = ((y[i] - dot(A[i, i+1:size(b)+1], x[i+1:size(b)+1])) / A[i,i])
    
    return x

def Inversa(A):

    B = zeros([size(A,1), size(A,1)])

    for i in range(size(A,1)):
        
        a = zeros(size(A,1))
        a[i] = 1

        B[:,i] = solve_LU(A, a)
    
    return B
        
def Newton(F,x0):
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

