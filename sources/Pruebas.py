from scipy.optimize import newton
from numpy import linspace, zeros, absolute

def Stability_region(T_S):
    
    return absolute(T_S(1.,1.,0.,P))

def P(U,t):
    N = 100
    R = linspace(-5,5,N)
    I = linspace(-5,5,N)
    w = zeros([N, N], dtype = complex)
    for i in range(N):
        for j in range(N):
            w[j,i] = complex(R[i], I[j])
    return w*U


def Crank_Nicolson(U, dt, t, F):
    
    def CN_res(x):
        
        return x - U_temp -dt/2 * F(x, t + dt)
    
    U_temp = U + dt/2 * F(U, t)
    
    return newton(CN_res, U)

S_R = Stability_region(Crank_Nicolson)