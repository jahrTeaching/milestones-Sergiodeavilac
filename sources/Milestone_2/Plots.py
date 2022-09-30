import matplotlib.pyplot as plt

def Plot_CP (U,t,Nd, T_S):
    
    fig, ax = plt.subplots(figsize=(4, 4))
    for i in range(Nd):
        dt = t[1]-t[0] 
        ax.plot(U[i,0,:], U[i,1,:], label= T_S + "dt" + str(dt[i]))
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title(T_S)
    ax.legend()
    plt.show()
    
   
    
def Plot_CP2 (U,t,Nd, T_S):
    
    fig, ax = plt.subplots(figsize=(4, 4))
    dt = t[1]-t[0] 
    ax.plot(U[0,:], U[1,:], label= T_S + "dt" + str(dt))
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title(T_S)
    ax.legend()
    plt.show()
    
def Plot_CP1 (U,t,Nd, T_S):
    
        
    
    fig, ax = plt.subplots(figsize=(4, 4))
    dt = t[1]-t[0] 
    ax.plot(U[0,:], U[1,:], label= T_S + "dt" + str(dt))
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title(T_S)
    ax.legend()
    plt.show()
    