from numpy import array

#Kepler
def Kepler(U, t): 

    x = U[0]; y = U[1]; dxdt = U[2]; dydt = U[3]
    d = ( x**2.0  + y**2.0 )**1.5
    print( type(x))
    print( type(y))

    return  array( [ dxdt, dydt, -x/d, -y/d ] ) 

        