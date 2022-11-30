from numpy.linalg import norm
from numpy import zeros, matmul, linspace

def ERK_sheme(U1 , dt, t, F):
    
    
    tolerance = 1e-6
    
    V1 = RK_scheme("First", F, t, dt, U1)
    V2 = RK_scheme("Second", F, t, dt, U1)
    
    (a, b, bs, c, q, Ne) = Butcher_array()
    
    h = min(dt, Step_size(V1 - V2, tolerance, min(q), dt))
    
    N = int(dt / h) + 1
    h = dt / N
    
    V1 = U1; V2 = U1
    
    for i in range(N):
        time = t + i * dt / N
        V1 = V2
        V2 = RK_scheme("First", F, time, h, V1)
    
    U2 = V2
    ierr = 0
    
    return U2

def Step_size(dU, tolerance, q, dt):
    if(norm(dU) > tolerance):
        return dt *( tolerance/norm(dU) )**(1 / (q+1) ) # Step_size
    else:
        return dt # Step_size
    
    

def RK_scheme(tag, F, t, dt, U1):
    
    (a, b, bs, c, q, Ne) = Butcher_array()
    N = len(U1)
    k = zeros([Ne, N])
    
    k[0,:] = F(U1, t + c[0]*dt)
    
    
    if tag == "First":
        
        for i in range(1,Ne):
            Up = U1
            
            for j in range(i):
                Up += dt * a[i,j]*k[j,:]
                
            k[i,:] = F(Up, t+c[i]*dt)
        
        U2= U1 + dt *matmul(b,k)
        
    elif tag == "Second":
        
        for i in range(1,Ne):
            Up = U1
            
            for j in range(i):
                Up += dt * a[i,j]*k[j,:]
                
            k[i,:] = F(Up, t + c[i] * dt)
            
        U2 = U1 + dt * matmul(bs,k)
    
    return U2

def Butcher_array():
    q = [5,4]
    Ne = 7 

    a = zeros([Ne,Ne-1])
    b = zeros([Ne])
    bs = zeros([Ne])
    c = zeros([Ne])
    
    c[:] = [ 0., 1./5, 3./10, 4./5, 8./9, 1., 1. ]

    a[0,:] = [          0.,           0.,           0.,         0.,           0.,     0. ]
    a[1,:] = [      1./5  ,           0.,           0.,         0.,           0.,     0. ]
    a[2,:]= [      3./40 ,        9./40,           0.,         0.,           0.,     0. ]
    a[3,:] = [     44./45 ,      -56./15,        32./9,         0.,           0.,     0. ]
    a[4,:] = [ 19372./6561, -25360./2187,  64448./6561,  -212./729,           0.,     0. ]
    a[5,:] = [  9017./3168,    -355./33 ,  46732./5247,    49./176, -5103./18656,     0. ]
    a[6,:]= [    35./384 ,           0.,    500./1113,   125./192, -2187./6784 , 11./84 ]

    b[:]  = [ 35./384   , 0.,   500./1113,  125./192,  -2187./6784  ,  11./84  ,     0.]
    bs[:] = [5179./57600, 0., 7571./16695,  393./640, -92097./339200, 187./2100, 1./40 ]
    
    return (a, b, bs, c, q, Ne)


   
