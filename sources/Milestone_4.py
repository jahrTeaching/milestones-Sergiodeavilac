from numpy import array, save, zeros, linspace, shape
from ODES.Cauchy_Problem import C_P
from Problems.Physics import Kepler, Linear_Oscilator
from ODES.Temporal_Schemes import Euler, RK4, Crank_Nicolson, Inverse_Euler, LeapFrog
from Stability_Region.S_R import Stability_Region
from Error.Richarson import Richarson, Convergence_rate
from alive_progress import alive_bar #to see the progress of the computations
import Graf.Plots as plt

#Initial Conditions
r0 = [1]
v0 = [0]
U0 = r0 + v0
T = 100
dt = [0.1, 0.01, 0.001]
# dt = [0.1, 0.15, 0.2]

#Save Plots
Save = True # True Save the plots / False show the plots

# # Temporal_Schemes to use
T_S = [Euler, RK4, Crank_Nicolson, Inverse_Euler, LeapFrog]
T_S_plot = ["Euler", "RK4", "CN", 'Euler_inver', "LeapFrog"]

# T_S = [LeapFrog]
# T_S_plot = ["LeapFrog"]


#Initiation of Dictionaries
Er_dic = { }
t_dic = { }
U_dic = { }     
S_R = { }
N = zeros((len(dt)))

#Iterations and times
for i in range(len(dt)):
        N[i] = int(T/dt[i])
        t_dic[str(i)] = linspace(0,T, int(N[i]))


# # #Simulations
# for j in range ( len(T_S_plot) ):
#         for x in t_dic: # x is a str and U is creating new keys
#                 U_dic[x]= C_P(Linear_Oscilator, t_dic[x], U0, T_S[j])
#                 plt.Plot_CP(U_dic[x], t_dic[x], T, dt[int(x)], T_S_plot[j], Save) # x return the value of the key
#         plt.Plot_CP_all(U_dic,t_dic,T, dt, T_S_plot[j], Save)
#         print(T_S_plot[j] + " calculado \n")

#Stability Region

for i in range( len(T_S_plot) ):
        S_R[i] = Stability_Region(T_S_plot[i])
        plt.Plot_SR(S_R[i], dt, T_S_plot[i], Save)