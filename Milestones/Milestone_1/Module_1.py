import numpy as np
import matplotlib.pyplot as plt
import Methods as MT

###########################################################
# Initial Values
###########################################################

r0 = [1,0]
v0 = [0,1]
U_0 = r0 + v0
N = 10000
DeltaT = 0.01
dt = [0.1, 0.01, 0.001]

U = np.zeros((len(dt), len(U_0), N+1)) #array of zeros
U_RK4 = np.zeros((len(dt), len(U_0), N+1))#array of zeros
U_CN = np.zeros((len(dt), len(U_0), N+1))#array of zeros

U[:,:,0] = U_0 #Initial conditions    
U_RK4[:,:,0] = U_0 #Initial conditions
U_CN[:,:,0] = U_0 #Initial conditions

###########################################################
# Simulations
###########################################################

# Euler aproximation
for i in range(len(dt)):
    U[i,:,:] = MT.Euler(U[i,:,:], N, dt[i]) 
    print('Euler ' + str(dt[i]) + ' done\n')
    
# Rugen-Kutta 4 order aproximation
for i in range(len(dt)): 
    U_RK4[i,:,:] = MT.RK4(U_RK4[i,:,:], N, dt[i])
    print('Rk4 ' + str(dt[i]) + ' done\n' )

# Crank-Nicolson aproximation
for i in range(len(dt)):
    U_CN[i,:,:] = MT.CN(U_CN[i,:,:], N, dt[i])
    print('CN ' + str(dt[i]) + ' done\n')

###########################################################
# Plots
###########################################################

#Plot 1
fig, ax = plt.subplots(figsize=(4, 4))
for i in range(len(dt)):
    ax.plot(U[i,0,:], U[i,1,:], label='Euler Method DeltaT' + str(dt[i]))
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Euler')
ax.legend()
plt.show()

#Plot 2
fig, ay = plt.subplots(figsize=(4,4))
for i in range(len(dt)):
    ay.plot(U_RK4[i,0,:], U_RK4[i,1,:], label='Runge-Kutta 4 DeltaT ' + str(dt[i]))
ay.set_xlabel('x')
ay.set_ylabel('y')
ay.set_title('RK4')
ay.legend()
plt.show()

#Plot 3
fig, az = plt.subplots(figsize=(4,4))
for i in range(len(dt)):
    az.plot(U_CN[i,0,:], U_CN[i,1,:], label='Crank-Nicolson DeltaT ' + str(dt[i]))
az.set_xlabel('x')
az.set_ylabel('y')
az.set_title('CN')
az.legend()
plt.show()
 
    