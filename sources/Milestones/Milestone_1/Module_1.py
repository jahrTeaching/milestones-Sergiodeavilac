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

U = np.zeros((len(U_0),N+1))
U[:,0] = U_0 

U = MT.Euler(U,N,DeltaT)

#Plot
fig, ax = plt.subplots()
ax.plot(U[0,:], U[1,:])

ax.set(xlabel='X', ylabel='Y')
ax.grid()

plt.show()
    