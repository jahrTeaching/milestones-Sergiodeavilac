from numpy import sqrt, linspace, zeros, absolute, array

def Stability_Region(T_S):
    N = 100
    R = linspace(-5,5,N)
    I = linspace(-5,5,N)
    w = zeros([N, N], dtype = complex)
    
    # for i in range(N):
    #     w[i] = complex(R[i], I[i]) 
    
    for i in range(N):
        for j in range(N):
            w[j,i] = complex(R[i], I[j])
    return absolute(Stability_polynomial(T_S, w))
    


def Stability_polynomial(T_S, w):
    
    if T_S == 'Euler':
        return 1 + w
    elif T_S == 'RK4':
        return  1 + w + w**2/2 + w**3/6 + w**4/24
    elif T_S == 'CN':
        return  (2+w) / (2-w)
    elif T_S == 'Euler_inver':
        return 1 / (1-w) 
    elif T_S == 'LeapFrog':
        return sqrt(1)
         