from numpy import array, reshape, zeros
from numpy.linalg import norm

#Kepler
def Kepler(U, t): 

    x = U[0]; y = U[1]; x_dot = U[2]; y_dot = U[3]
    d = ( x**2  + y**2 )**1.5

    return  array( [ x_dot, y_dot, -x/d, -y/d ] ) 


def Linear_Oscilator(U,t):
    
    return array([U[1], -U[0]])



def N_B(U,t): # N-Bodies problem 
    
    Nc = 3
    Nb = int(len(U) / (2*Nc))
    
    # (Nb, Nc) = (4,3)
    
    Us = reshape( U, (Nb, Nc, 2) ) # Tensor Nb, Nc, (Position, Velocity)
    
    r = reshape( Us[:,:,0], (Nb, Nc) ) # Matrix Position 
    v = reshape( Us[:,:,1], (Nb, Nc) ) # Matrix Velocity
    
    F = zeros( len(U) )
    Fs = reshape( F, (Nb, Nc, 2) ) # Tensor Nb, Nc, (Position, Velocity) 
    
    drdt = reshape( Fs[:,:,0], (Nb,Nc) ) # Matrix Velocity
    dvdt = reshape( Fs[:,:,1], (Nb,Nc) ) # Matrix Acceleration
    
    dvdt[:,:] = 0
    
    for i in range(Nb):
        drdt[i,:] = v[i,:]
        for j in range(Nb):
            if j != i:
                d = r[j,:] - r[i,:]
                dvdt[i,:] +=  d[:]/( norm(d)**3)
            
    return F