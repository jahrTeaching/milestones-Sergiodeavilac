from numpy import sqrt, zeros, array
from numpy.linalg import eig
from scipy.optimize import newton, fsolve
from ODES.Jab_Newt import Newton, Jacobiano

def RBP(U, t, mu): # Arenstorf_equations
    
    r = U[:2] #Position
    drdt = U[2:] #Velocity

    p1 = sqrt( ( r[0] + mu )**2 + r[1]**2 )
    p2 = sqrt( (r[0] - 1 + mu)**2 + r[1]**2 )

    dvdt_1 = - ( 1 - mu ) * ( r[0] + mu ) / ( p1**3 ) - mu*( r[0] - 1 + mu ) / ( p2**3 )
    dvdt_2 = - ( 1 - mu ) * r[1] / ( p1**3 ) - mu*r[1] / ( p2**3 )

    return array( [ drdt[0], drdt[1], 2*drdt[1] + r[0] + dvdt_1, -2*drdt[0] + r[1] + dvdt_2] )

def Lagrange_Points(U0, N_LP, mu):

    LP = zeros( [5,2] )

    def F(Y):
        X = zeros(4)
        X[:2] = Y
        X[2:] = 0
        FX = RBP(X, 0 , mu)
        return FX[2:4]
   
    for i in range(N_LP):
        LP[i,:] = fsolve( F, U0[i,:2] )
        
    return LP

def stb_Lp(U_0, mu):

    def F(Y):
        return RBP(Y, 0 , mu)

    J = Jacobiano(F, U_0)
    
    Autovalor, autovector = eig(J)

    return Autovalor
