from numpy import array, linspace, zeros, size, shape, log10
from numpy.linalg import norm
from alive_progress import alive_bar #to see the progress of the computations
from scipy.stats import linregress


def Richarson(U0, t1, F, T_S, problem, order):
    
    N = size(t1) - 1 #Because of the divisons of the time's linspace (Python begin at 0)

    t2 = linspace(0, t1[-1],2*size(t1))
    Er = zeros( (len(U0), N+1) )
    
    # for i in range(N): # 0 to N-1
    #     t2[2*i] = t1[i]
    #     t2[2*i + 1] = ( t1[i] + t1[i+1] ) / 2
       
    # t2[2*N] = t1[N]
    
    U1 = problem(F, t1, U0, T_S)
    U2 = problem(F, t2, U0, T_S)

    for i in range(N):
        Er[:, i] = ( U2[:, 2*i]- U1[:,i] ) / ( 1 - 1./2** order )

    return Er

def Convergence_rate(U0, t1, F, T_S, problem):
    
    m = 10 #number of points
    N = size(t1) - 1
    Nt2 = size(t1)
    U1= problem(F, t1, U0, T_S)
    
    log_Er = zeros(m); log_N = zeros(m)
    
    # for i in range(N): # 0 to N-1
    #     t2[2*i] = t1[i]
    #     t2[2*i + 1] = ( t1[i] + t1[i+1] ) / 2
       
    # t2[2*N] = t1[N]

    U2 = zeros( shape(U1) )
    with alive_bar(m) as bar:
        for i in range(m):
            Nt2 = 2*Nt2
            t2 = linspace(0, t1[-1],Nt2) #t[-1] return the last value of the vector or list
            U2 = problem(F, t2, U0, T_S)
            log_Er[i] = log10(norm(  U2[:, -1]- U1[:,-1] ) )
            log_N[i] = log10(Nt2)
            t1 = t2
            U1 = U2
            bar()
            
    regress = linregress(log_N, log_Er) #Its's a object with all the information
    order = regress.rvalue**2
            
    return log_Er, log_N, regress
    
    
    

    