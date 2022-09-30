from numpy import zeros, linspace, shape
import Temporal_Schemes as TS
from Cauchy_Problem import C_P
from Physics import Kepler
from Plots import Plot_CP1, Plot_CP2
# from Plots import Plot_CP, Plot_CP1


#Initial Conditions
r0 = [1.0,0.0]
v0 = [0.0,1.0]
U0 = r0 + v0
N = [1000, 10000, 100000]
Nd = 3 #Number of diferent dt
T_S = [TS.Euler, TS.RK4]
T_S_plot = ["Euler", "RK4"]

#Initiation of arrays 
U_dic = { }
t_dic = {
        't1': linspace(0,20,N[0]), 
        't2': linspace(0,20,N[1]), 
        't3': linspace(0,20,N[2])
        }

for j in range ( len(T_S_plot) ):
    for x in t_dic:
        
        U_dic[x]= C_P(Kepler, t_dic[x], U0, T_S[j])
        print(T_S_plot[j] + " calculado \n")
        Plot_CP1(U_dic[x],t_dic[x], Nd, T_S_plot[j])


    
    
    
    
    
    
# t1 = linspace(0,20,N[0])
# t2 = linspace(0,20,N[1])
# t3 = linspace(0,20,N[2])

# #Cauchy Problem
# #Euler
# U = C_P(Kepler, t1, U0, T_S[0])
# Plot_CP1(U,t1, Nd, T_S_plot[0])
# U = C_P(Kepler, t2, U0, T_S[0])
# Plot_CP1(U,t2, Nd, T_S_plot[0])
# U = C_P(Kepler, t3, U0, T_S[0])
# Plot_CP1(U,t3, Nd, T_S_plot[0])

    




