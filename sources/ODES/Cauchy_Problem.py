from numpy import array, zeros

def C_P(F, t, U0, T_S):
    
    N = len(t)-1 #Because of the divisons of the time's linspace 
    U = zeros( (len(U0), N+1 ) ) #len will give you the number of 'elements' of the first dimension (4)
    U[:,0] = U0
    
    for i in range(N):
        
        U[:, i+1] = T_S(U[:,i], t[i+1]-t[i], t[i], F)
    
    return U
    