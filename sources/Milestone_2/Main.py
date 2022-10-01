from numpy import zeros, linspace, shape
from Cauchy_Problem import C_P
from Physics import Kepler
from Plots import Plot_CP
from Temporal_Schemes import Euler, RK4, CN, Euler_inver


#Initial Conditions
r0 = [1,0]
v0 = [0,1]
U0 = r0 + v0
N = [1000, 10000, 100000]

#Save Plots
Save = False # TRue Save the plots / False show the plots

#Temporal_Schemes to use
# T_S = [Euler, RK4, CN, Euler_inver]
# T_S_plot = ["Euler", "RK4", "CN", 'Euler_inver']
T_S = [Euler_inver]
T_S_plot = ['Euler_inver']

#Initiation of Dictionaries
U_dic = { }
t_dic = { }

#Times for simulations
for i in range(len(N)):
        t_dic[str(i)] = linspace(0,20,N[i])
                  
#Simulations
for j in range ( len(T_S_plot) ):
        for x in t_dic: # x is a str and U is creating new keys
                U_dic[x]= C_P(Kepler, t_dic[x], U0, T_S[j])
                print(T_S_plot[j] + " calculado \n")
                Plot_CP(U_dic[x],t_dic[x], T_S_plot[j], Save) # x return the value of the key
