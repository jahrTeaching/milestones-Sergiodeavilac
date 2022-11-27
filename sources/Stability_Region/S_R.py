from numpy import sqrt, linspace, zeros, absolute, array

def Stability_Region(T_S):
    N = 100
    R = linspace(-5,5,N)
    I = linspace(-5,5,N)
    w = zeros([N, N], dtype = complex)
    for i in range(N):
        for j in range(N):
            w[j,i] = complex(R[i], I[j])

    if T_S.__name__ == "LeapFrog":
        return absolute( T_S(1,1,1,0, lambda U, t: w*U) )
    else:
        return absolute( T_S(1,1,0, lambda U, t: w*U) )
