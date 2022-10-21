from numpy import zeros, linspace, shape
from ODES.Cauchy_Problem import C_P
from Problems.Physics import Kepler
from ODES.Temporal_Schemes import Euler, RK4, Crank_Nicolson, Inverse_Euler
from Error.Richarson import Richarson, Convergence_rate
from alive_progress import alive_bar #to see the progress of the computations
import Graf.Plots as plt


#Initial Conditions
r0 = [1,0]
v0 = [0,1]
U0 = r0 + v0
T = 100
dt = [0.01]
# dt = [0.1, 0.15, 0.2]

#Save Plots
Save = True # True Save the plots / False show the plots

# Temporal_Schemes to use
# T_S = [Euler, RK4, Crank_Nicolson, Inverse_Euler]
# T_S_plot = ["Euler", "RK4", "CN", 'Euler_inver']
# Order = [1, 4, 2, 1]
T_S = [Inverse_Euler]
T_S_plot = ["Euler_inver"]
Order = [1]

#Initiation of Dictionaries
Er_dic = { }
t_dic = { }
U_dic = { }
N = zeros((len(dt)))

#Iterations and times
for i in range(len(dt)):
        N[i] = int(T/dt[i])
        t_dic[str(i)] = linspace(0,T, int(N[i]))

with alive_bar(len(T_S)) as bar:
        for j in range(len(T_S)):
                for x in t_dic:
                        Er_dic[x] = Richarson(U0, t_dic[x], Kepler, T_S[j], C_P, Order[j])
                        plt.Plot_Er(Er_dic[x], t_dic[x], T, dt[int(x)], T_S_plot[j], Save)
                plt.Plot_Er_compare(Er_dic, t_dic, T, dt, T_S_plot[j], Save)
                print(T_S_plot[j] + " calculado \n")
                bar()

# for j in range(len(T_S)): 
#     for x in t_dic:
#         log_Er, log_N, regress = Convergence_rate(U0, t_dic[x], Kepler, T_S[j], C_P)
#         print( '\n' +T_S_plot[j] + ' Calculado \n' )
#         plt.Plot_Conv_Rat(log_N, log_Er, T, dt[int(x)],regress, T_S_plot[j], Save)

# # #Simulations
# with alive_bar(len(T_S)) as bar:
#         for j in range ( len(T_S_plot) ):
#                 for x in t_dic: # x is a str and U is creating new keys
#                         U_dic[x]= C_P(Kepler, t_dic[x], U0, T_S[j])
#                         plt.Plot_CP(U_dic[x], T, dt[int(x)], t_dic[x], T_S_plot[j], Save) # x return the value of the key
#                 plt.Plot_CP_all(U_dic,t_dic,T, dt, T_S_plot[j], Save)
#                 print(T_S_plot[j] + " calculado \n")
#                 bar()
