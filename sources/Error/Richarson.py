from numpy import array, zeros, size, shape

def Richarson(U0, t_domian, F, T_S, problem, order):
    N = size(t_domian) - 1 #Because of the divisons of the time's linspace 
    U1 = zeros( (len(U0), N+1 ) ); U2 = zeros( (len(U0), N+1 ) )
    t1 = t_domian
    t2 = zeros( (2*len(t1)) )
    Er = zeros( (len(U0), N+1) )
    for i in range(N): # 0 to N-1
        t2[2*i] = t1[i]
        t2[2*i + 1] = ( t1[i] + t1[i+1] ) / 2
        
    t2[2*N] = t1[N]
    U1= problem(F, t1, U0, T_S)
    U2 = problem(F, t2, U0, T_S)
    
    for i in range(N, -1):
        U1[:, i] = U1[:, i] + 2 * U1[:, i-1] + U1[:, i-2] / 4
        
    for i in range(2*N,-1):
        U2[:, i] = ( U2[:, 2*i] + 2 * U2[:, i-1] + U2[:, i-2] ) / 4

    for i in range(N):
        Er[:, i] = ( U2[:, 2*i]- U1[:,i] ) / ( 1 - 1./2** order )

    return Er


    
    