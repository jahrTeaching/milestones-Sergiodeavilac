import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

#Function F
def Func(U): #U must be a vector
    F1 = U[2]
    F2 = U[3]
    F3 = -U[0] / (U[0]**2 + U[1]**2)**(3/2)
    F4 = -U[1] / (U[0]**2 + U[1]**2)**(3/2)
    F = [F1, F2, F3, F4]
    return F

#Euler_Method###########################################
def Euler(U, N, DeltaT):
    
    for i in range(N):
        F = Func(U[:, i])
        F = np.array(F)
        U_v = np.array(U[:, i])
        U_v = U_v + DeltaT*F
        U[:, i+1] = U_v
    return U

#Crank-Nicolson#########################################
def CN(U, N, DeltaT):
    
    for i in range(N):
        F = np.array(Func(U[:, i]))
        U_v = np.array(U[:, i])
        U_v = U_v + DeltaT/2*(F)   
        U[:, i+1] = U_v
    return U

#Runge-Kutta segundo orden##############################  
def RK2(U, N, DeltaT):
    
    for i in range(N):
        k1 = np.array(Func(U[:, i]))
        k2 = np.array(Func(U[:, i] + DeltaT * k1))
        U_v = np.array(U[:, i])
        U_v = U_v + DeltaT/2 * (k1 + k2)
        U[:, i+1] = U_v
    return U

#Runge-Kutta cuarto orden##############################  
def RK4(U, N, DeltaT):
    
    for i in range(N):
        k1 = np.array(Func(U[:, i]))
        k2 = np.array(Func(U[:, i] + DeltaT * k1 / 2))
        k3 = np.array(Func(U[:, i] + DeltaT * k2 / 2))
        k4 = np.array(Func(U[:, i] + DeltaT * k3))
        U_v = np.array(U[:, i])
        U_v = U_v + DeltaT/6 * (k1 + 2 * k2 + 2 * k3 + k4)
        U[:, i+1] = U_v
    return U

#Crank-Nicolson#########################################
def CN(U, N, DeltaT):
    for i in range(N):
        F = np.array(Func(U[:, i]))
        F1 = np.array(Func(U[:, i+1]))
        U_ = np.array(U[:, i])
        def Crank (U1):
            return U1 - U_ - (DeltaT / 2) * (F1 + F)
        U[:, i+1] = fsolve(Crank, U_)
    return U
        