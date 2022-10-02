from numpy import array

#Kepler
def Kepler(U, t): 

    x = U[0]; y = U[1]; x_dot = U[2]; y_dot = U[3]
    d = ( x**2  + y**2 )**1.5

    return  array( [ x_dot, y_dot, -x/d, -y/d ] ) 

        