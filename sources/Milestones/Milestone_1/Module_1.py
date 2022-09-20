import numpy as np
import matplotlib.pyplot as plt
import Methods as MT

#Initial Values
r0 = [1,0]
v0 = [0,1]
U_0 = r0 + v0
N = 10000
DeltaT = 0.01
dt = [0.1, 0.01, 0.001]

U = np.zeros((len(dt), len(U_0), N+1)) #array of zeros
U_RK4 = np.zeros((len(dt), len(U_0), N+1))#array of zeros
U_CN = np.zeros((len(U_0), N+1))#array of zeros

U[:,:,0] = U_0 #Initial conditions    
U_RK4[:,:,0] = U_0 #Initial conditions
U_CN[:,0] = U_0

#Simulations
for i in range(len(dt)):
    U[i,:,:] = MT.Euler(U[i,:,:], N, dt[i]) #Euler aproximation
    print('Euler ' + str(dt[i]) + ' done\n')

for i in range(len(dt)): #Rugen-Kutta 4 order aproximation
    U_RK4[i,:,:] = MT.RK4(U_RK4[i,:,:], N, dt[i])
    print('Rk4 ' + str(dt[i]) + ' done\n' )

U_CN = MT.CN(U_CN, N, dt[1])
print(str(U_CN))
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

#Plot 3
fig, az = plt.subplots(figsize=(4,4))
#for i in range(len(dt)):
az.plot(U_CN[0,:], U_CN[1,:])
az.set_xlabel('x')
az.set_ylabel('y')
az.set_title('CN')
az.legend()
plt.show()
 
    