from re import X
from numpy import array, zeros, shape
from scipy.optimize import newton
import matplotlib.pyplot as plt

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
def CN(U, dt, t, F):
    
    def CN_res(X):
        
        return X - a -dt/2 * F(X, t + dt)
    
    a = U - dt/2 * F(U, t)
    
    return newton(CN_res, U)

        