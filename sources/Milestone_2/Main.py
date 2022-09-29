from numpy import zeros, linspace
import Temporal_Schemes
from Physics import Kepler
import matplotlib.pyplot as plt
r0 = [1.0,0.0]
v0 = [0.0,1.0]
U0 = r0 + v0
dt = 
U = zeros((len(dt), len(U0), N+1))
U[:,:,0] = U0
t = 0