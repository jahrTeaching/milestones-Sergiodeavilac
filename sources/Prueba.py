from numpy import array, zeros, linspace
import matplotlib.pyplot as plt



def abstraction_for_F_and_Euler(): 

    U = array( [ 1, 0, 0, 1 ])
    
    N = 200 
    x = array( zeros(N) )
    y = array( zeros(N) )
    t = array( zeros(N) )
    x[0] = U[0] 
    y[0] = U[1]
    t[0] = 0 
    
    for i in range(1, N): 

      dt = 0.1 
      t[i] = dt*i
      U = Euler(U, dt, t, Kepler)
      x[i] = U[0] 
      y[i] = U[1]
    
    plt.plot(x, y)
    plt.show()

def Kepler(U, t): 

    x = U[0]; y = U[1]; dxdt = U[2]; dydt = U[3]
    d = ( x**2  +y**2 )**1.5

    return  array( [ dxdt, dydt, -x/d, -y/d ] ) 

def Euler(U, dt, t, F): 

    return U + dt * F(U, t)

abstraction_for_F_and_Euler()