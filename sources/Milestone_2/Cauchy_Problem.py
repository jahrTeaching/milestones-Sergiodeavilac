from numpy import array, zeros

def C_P(F, t, U0,T_S):
    
    N = len(t)-1 #Because of the divisons of the time's linspace 
    U = zeros( (len(U0), N+1 ) )
    U[:,0] = U0
     
    dt = t[1] - t[0] 
    for i in range(N):
        
        U[:, i+1] = T_S(U[:,i] , dt, t[i], F)
    
    return U
    