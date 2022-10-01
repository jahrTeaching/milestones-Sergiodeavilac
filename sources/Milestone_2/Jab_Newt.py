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

