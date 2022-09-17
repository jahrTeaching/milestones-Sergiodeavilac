import numpy as np
import matplotlib.pyplot as plt
import Methods as MT
#Euler method###############################

#Initial Values
r0 = [1,0]
v0 = [0,1]
U_0 = r0 + v0
N = 10000
DeltaT = 0.01
dt = [0.1, 0.01, 0.001]

U = np.zeros((len(dt), len(U_0), N+1)) #array of zeros
U_RK4 = np.zeros((len(dt), len(U_0), N+1))#array of zeros

U[:,:,0] = U_0 #Initial conditions    
U_RK4[:,:,0] = U_0 #Initial conditions

for i in range(len(dt)):
    U[i,:,:] = MT.Euler(U[i,:,:],N,dt[i]) #Euler aproximation
    print('Euler ' + str(dt[i]) + ' done\n')

for i in range(len(dt)): #Rugen-Kutta 4 order aproximation
    U_RK4[i,:,:] = MT.RK4(U_RK4[i,:,:],N,dt[i])
    print('Rk4 ' + str(dt[i]) + ' done\n' )

#Plot 1
fig, ax = plt.subplots(figsize=(4,4))
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
 
    