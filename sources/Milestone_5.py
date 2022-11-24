from numpy import array, save, zeros, linspace, shape, reshape, transpose
from ODES.Cauchy_Problem import C_P
from Problems.Physics import N_B, split, join
from ODES.Temporal_Schemes import Euler, RK4, Crank_Nicolson, Inverse_Euler, LeapFrog
import Graf.Plots as plt


#Initial Conditions
(Nb, Nc) = (4,3)

r0 = zeros( (Nb, Nc) )
v0 = zeros( (Nb, Nc) )
r0[0,:] = [1,0,0]; r0[1,:] = [-1,0,0]; r0[2, :] = [ 0, 1, 0 ]; r0[3, :] = [ 0, -1, 0 ] # Position
v0[0,:] = [0, 0.4, 0]; v0[1,:] = [0, -0.4, 0]; v0[2, :] = [ -0.4, 0., 0. ]; v0[3, :] = [ 0.4, 0., 0. ] # Velocity



U0 = join(r0, v0, Nc, Nb)


#Save Plots
Save = False # True Save the plots / False show the plots

#Iterations and times
N = 10000
T = 10
t = linspace(0,T,N+1)

# Simulations

U = transpose( C_P(N_B, t, U0, RK4, "RK4") )

   
r = split(U)
   
plt.Plot_NBodies(r, t, T, 15/1000, "Rk4", Save) # x return the value of the key
