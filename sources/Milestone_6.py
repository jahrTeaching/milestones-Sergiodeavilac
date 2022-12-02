from numpy import array, save, zeros, linspace, shape, reshape, around
from ODES.Cauchy_Problem import C_P, C_P_line
from Problems.NB3_restrict import RBP, Lagrange_points, stb_Lp
from Problems.Physics import N_B, split, join
from ODES.Temporal_Schemes import Euler, RK4, Crank_Nicolson, Inverse_Euler, LeapFrog
from ODES.ERK import ERK_sheme
from random import random
import Graf.Plots as plt

# Save plot
Save = False

# Temporal_Scheme

T_S = T_S = [Euler, RK4, Crank_Nicolson, Inverse_Euler, LeapFrog, ERK_sheme]

# Data of the system
mu_earth_Moon = 1.2151e-2

#Initial Conditions for interpolation
N = 10000
t = linspace(0, 100, N)

U0 = zeros( [5,4] ) # Number of Lagrange points and coordiantes

U0[0,:] = [0.8, 0.6, 0 , 0]
U0[1,:] = [0.8, -0.6, 0, 0]
U0[2,:] = [-0.1, 0, 0, 0]
U0[3,:] = [0.1, 0, 0, 0]
U0[4,:] = [1.01, 0, 0, 0]

L_p = Lagrange_points(U0, 5, mu_earth_Moon)
print("\n" + str(L_p) + "\n")

#Stability of Lagrande Points
L_p_stb = zeros( 4 )

for i in range( len(L_p_stb) ):
    L_p_stb[:2] = L_p[i, :]
    stb = around( stb_Lp(L_p_stb, mu_earth_Moon), 5)
    print(str(stb) + "\n")

#Lagrange Point's Orbits

U_0LPO = zeros( [shape(U0)[0], 4] )

eps = 1e-3 # Perturbación para poder obtener el movimiento

for i in range( shape(U0)[0] ):
    U_0LPO[i, :2] = L_p[i, :] + eps
    U_0LPO[i, 2:] = eps

def F(U,t):
   return RBP(U, t, mu_earth_Moon)

for j in range ( len(T_S) ):
    for i in range( shape(U0)[0] ):
        U_LP = C_P(F, t, U_0LPO[i,:], T_S) # Opción 1#Meto fila y me devuelve en columnas
        plt.Plot_LPO(U_LP, L_p, mu_earth_Moon, i, Save)
