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
def CN(U, N, delta_t):
    for i in range(0,N):
        U1 = U[:,i]
        def func_CN(x):
            return [x[0] - U1[0] - (x[2] + Func(U1)[0])*delta_t/2,
                    x[1] - U1[1] - (x[3] + Func(U1)[1])*delta_t/2,
                    x[2] - U1[2] - (-x[0]/(x[0]**2+x[1]**2)**(3/2) + Func(U1)[2])*delta_t/2,
                    x[3] - U1[3] - (-x[1]/(x[0]**2+x[1]**2)**(3/2) + Func(U1)[3])*delta_t/2]
        U[:,i+1] = fsolve(func_CN, [U[0,i], U[1,i], U[2,i], U[3,i]])
    return(U)

        