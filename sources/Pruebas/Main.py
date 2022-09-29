from numpy import zeros, linspace
import Temporal_Schemes
from Physics import Kepler
import matplotlib.pyplot as plt
r0 = [1,0]
v0 = [0,1]
U0 = r0 + v0
N = 10000
dt = [0.01]
U = zeros((len(dt), len(U0), N+1))
U[:,:,0] = U0
t = 0

# for j in range(len(dt)):
#     for i in range(N):
#         U[j,:,i] =Temporal_Schemes.Euler(U[j,:,i],dt[j],t, Kepler)
        
for i in range(N):
    U[0,:, i] =Temporal_Schemes.Euler(U[0,:,i],dt[0],t, Kepler)

fig, ax = plt.subplots(figsize=(4, 4))
for i in range(len(dt)):
    ax.plot(U[i,0,:], U[i,1,:], label='Euler Method DeltaT' + str(dt[i]))
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Euler')
ax.legend()
plt.show()

