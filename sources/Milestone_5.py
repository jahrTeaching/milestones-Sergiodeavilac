from numpy import array, save, zeros, linspace, shape, reshape, transpose
from ODES.Cauchy_Problem import C_P
from Problems.Physics import N_B
from ODES.Temporal_Schemes import Euler, RK4, Crank_Nicolson, Inverse_Euler, LeapFrog
import Graf.Plots as plt


#Initial Conditions
(Nb, Nc) = (4,3)

U0 =  zeros(2*Nc*Nb)
U1  = reshape( U0, (Nb, Nc, 2) )  
r0 = reshape( U1[:, :, 0], (Nb, Nc) )   # Position
v0 = reshape( U1[:, :, 1], (Nb, Nc) )   # Velocity

# r0[0,:] = [1,0,0]; r0[1,:] = [-1,0,0]; r0[2, :] = [ 0, 1, 0 ]; r0[3, :] = [ 0, -1, 0 ] # Position
# v0[0,:] = [0, 0.4, 0]; v0[1,:] = [0, -0.4, 0]; v0[2, :] = [ -0.4, 0., 0. ]; v0[3, :] = [ 0.4, 0., 0. ] # Velocity
r0[0,:] = [0,0,1]; r0[1,:] = [-1,0,0]; r0[2, :] = [ 0, 1, 0 ]; r0[3, :] = [ 0, -1, 0 ] # Position
v0[0,:] = [0, 0.4, 0]; v0[1,:] = [0, -0.4, 0]; v0[2, :] = [ -0.4, 0., 0. ]; v0[3, :] = [ 0.4, 0., 0. ] # Velocity

#Save Plots
Save = False # True Save the plots / False show the plots

#Iterations and times
N = 10000
T = 10
t = linspace(0,T,N+1)

# Simulations

U = C_P(N_B, t, U0, RK4, "RK4")
U = transpose(U)

Us = reshape( U, (N+1, Nb, Nc, 2) )
r = reshape( Us[:, :, :, 0], (N+1, Nb, Nc) )

# for i in range(Nb):
#         plt.plot(  r[:, i, 0], r[:, i, 1] )
# plt.axis('equal')
# plt.grid()
# plt.show()
   
plt.Plot_NBodies(r, t, T, 15/1000, "Rk4", Save) # x return the value of the key
