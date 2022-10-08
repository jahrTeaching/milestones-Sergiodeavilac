from numpy import zeros, linspace, shape
from ODES.Cauchy_Problem import C_P
from Problems.Physics import Kepler
from Graf.Plots import Plot_CP, Plot_CP_all
from ODES.Temporal_Schemes import Euler, RK4, Crank_Nicolson, Inverse_Euler
from Error.Richarson import Richarson


#Initial Conditions
r0 = [1,0]
v0 = [0,1]
U0 = r0 + v0
N = [1000]

#Save Plots
Save = False # TRue Save the plots / False show the plots

#Temporal_Schemes to use
# T_S = [Euler, RK4, Crank_Nicolson, Inverse_Euler]
# T_S_plot = ["Euler", "RK4", "CN", 'Euler_inver']
# Order = [1, 4, 2, 1]
T_S = [Euler]
Order = [1]

#Initiation of Dictionaries
U_dic = { }
t_dic = { }

#Times for simulations
for i in range(len(N)):
        t_dic[str(i)] = linspace(0,20,N[i])

for x in t_dic:
    Er = Richarson(U0, t_dic[x], Kepler, T_S, C_P, Order)

#Simulations
# for j in range ( len(T_S_plot) ):
#         for x in t_dic: # x is a str and U is creating new keys
#                 U_dic[x]= C_P(Kepler, t_dic[x], U0, T_S[j])
#                 print(T_S_plot[j] + " calculado \n")
#                 # Plot_CP(U_dic[x],t_dic[x], T_S_plot[j], Save) # x return the value of the key
#         Plot_CP_all(U_dic,t_dic, T_S_plot[j], Save) 