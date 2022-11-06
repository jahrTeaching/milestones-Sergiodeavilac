from numpy import array, zeros

def C_P(F, t, U0, T_S, T_S_plot):
    
    N = len(t)-1 #Because of the divisons of the time's linspace 
    U = zeros( (len(U0), N+1 ) ) #len will give you the number of 'elements' of the first dimension (4)
    U[:,0] = U0
    
    if T_S_plot == "LeapFrog":
        for i in range(N):
            dt = t[i+1]-t[i]
            if t[i] == 0:
                U[:,1] = U[:,0] + dt*F(U[:,0],t)
            else:
                U[:,i+1] = T_S(U[:,i], U[:,i-1], dt, t[i], F)
    else:
        for i in range(N):
            dt = t[i+1]-t[i]
            U[:, i+1] = T_S(U[:,i], dt, t[i], F)

        
    return U
    