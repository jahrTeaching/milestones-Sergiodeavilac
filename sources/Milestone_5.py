from numpy import array, save, zeros, linspace, shape
from ODES.Cauchy_Problem import C_P
from Problems.Physics import N_B
from ODES.Temporal_Schemes import Euler, RK4, Crank_Nicolson, Inverse_Euler, LeapFrog
import Graf.Plots as plt


#Initial Conditions
r01 = [1,1,0]; r02 = [0,0,1]
v01 = [0,1,0]; v02 = [0,1,0]
U0 = r01 + v01 + r02 + v02 # Concatenation of initical conditions
T = 10
dt = [0.1]

#Save Plots
Save = False # True Save the plots / False show the plots

#Initiation of Dictionaries
t_dic = { }
U_dic = { }     
S_R = { }
N = zeros( (len(dt)) ) 

#Iterations and times
for i in range(len(dt)):
        N[i] = int(T/dt[i])
        t_dic[str(i)] = linspace(0,T, int(N[i]))

# Simulations

for j in range ( len(dt) ):
        for x in t_dic: # x is a str and U is creating new keys
                U_dic[x]= C_P(N_B, t_dic[x], U0, RK4, "RK4")
                print( U_dic[x] )
                plt.Plot_NBodies(U_dic[x], t_dic[x], T, dt[int(x)], "Rk4", Save) # x return the value of the key
        # plt.Plot_CP_all(U_dic, t_dic, T, dt, RK4, Save)
        print(" calculado \n")
        
