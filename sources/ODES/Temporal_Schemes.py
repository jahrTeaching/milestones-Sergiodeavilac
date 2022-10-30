from numpy import array, zeros, shape, size
from scipy.optimize import fsolve
from ODES.Jab_Newt import Newton, Newton_LU

#Euler_Method###########################################
def Euler(U , dt, t, F):
    
    return U + dt * F(U,t)

#Runge-Kutta cuarto orden##############################  
def RK4(U, dt, t, F):
        
    k1 = F(U,t)
    k2 = F(U + dt * k1 / 2, t)
    k3 = F(U + dt * k2 / 2, t)
    k4 = F(U + dt * k3, t)
        
    return U + dt/6 * (k1 + 2 * k2 + 2 * k3 + k4)

#Crank-Nicolson#########################################
def Crank_Nicolson(U, dt, t, F):
    
    def CN_res(x):
        
        return x - U_temp -dt/2 * F(x, t + dt)
    
    U_temp = U + dt/2 * F(U, t)
    
    return fsolve(CN_res, U)

#Euler_inverso#########################################
def Inverse_Euler(U, dt, t, F):
    def Euler_res(x):
        
        return x - U - dt*F(x,t)

    return Newton_LU(Euler_res, U)

#LeapFrog
def LeapFrog(U, dt, t, F):
     
    N = int(len(U)/2)
    X = U
    A = F(X,t)
    X[N:] += A[N:]*dt / 2
    X[:N] += X[:N]*dt
    A = F(X,t)
    X[N:] += A[N:]*dt / 2
    
    return X