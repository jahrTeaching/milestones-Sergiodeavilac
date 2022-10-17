from numpy import zeros, linspace, shape
from ODES.Cauchy_Problem import C_P
from Problems.Physics import Kepler
from ODES.Temporal_Schemes import Euler, RK4, Crank_Nicolson, Inverse_Euler
from Error.Richarson import Richarson, Convergence_rate
import Graf.Plots as plt


#Initial Conditions
r0 = [1,0]
v0 = [0,1]
U0 = r0 + v0
T = 10
dt = [0.1, 0.01, 0.001]
# dt = [0.1, 0.15, 0.2]

#Save Plots
Save = True # TRue Save the plots / False show the plots

#Temporal_Schemes to use
T_S = [Euler, RK4, Crank_Nicolson, Inverse_Euler]
T_S_plot = ["Euler", "RK4", "CN", 'Euler_inver']
Order = [1, 4, 2, 1]
# T_S = [RK4]
# T_S_plot = ["RK4"]
# Order = [1]

#Initiation of Dictionaries
Er_dic = { }
t_dic = { }
N = zeros((len(dt)))

#Times for simulations
for i in range(len(dt)):
        N[i] = int(T/dt[i])
for i in range(len(N)):
        t_dic[str(i)] = linspace(0,T, int(N[i]))

# for j in range(len(T_S)):
#         for x in t_dic:
#                 Er_dic[x] = Richarson(U0, t_dic[x], Kepler, T_S[j], C_P, Order[j])
#                 print(T_S_plot[j] + " calculado \n")
#                 plt.Plot_Er(Er_dic[x], t_dic[x],dt[int(x)], T_S_plot[j], Save)
#         plt.Plot_Er_compare(Er_dic, t_dic, dt, T_S_plot[j], Save)

for j in range(len(T_S)): 
    for x in t_dic:
        log_Er, log_N, regress = Convergence_rate(U0, t_dic[x], Kepler, T_S[j], C_P)
        print( '\n' +T_S_plot[j] + ' Calculado \n' )
        plt.Plot_Conv_Rat(log_N, log_Er, T, dt[int(x)],regress, T_S_plot[j], Save)

