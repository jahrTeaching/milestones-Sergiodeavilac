from numpy import zeros, linspace, shape
from Cauchy_Problem import C_P
from Physics import Kepler
from Plots import Plot_CP
from Temporal_Schemes import Euler, RK4, CN


#Initial Conditions
r0 = [1.0,0.0]
v0 = [0.0,1.0]
U0 = r0 + v0
N = [1000, 10000, 100000]
 #Number of diferent dt
T_S = [Euler, RK4, CN]
T_S_plot = ["Euler", "RK4", "CN"]
Nd = len(T_S)
#Initiation of Dictionaries
U_dic = { }
t_dic = { }

for i in range(len(N)):
        t_dic[str(i)] = linspace(0,20,N[i])
                  
for j in range ( len(T_S_plot) ):
        for x in t_dic: # x is a str and U is creating new keys
                U_dic[x]= C_P(Kepler, t_dic[x], U0, T_S[j])
                print(T_S_plot[j] + " calculado \n")
                Plot_CP(U_dic[x],t_dic[x], Nd, T_S_plot[j]) # x return the value of the key
