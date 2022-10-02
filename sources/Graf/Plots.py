import matplotlib.pyplot as plt
import os


def Plot_CP(U,t, T_S, Save):
    fig, ax = plt.subplots(figsize=(4, 4))
    dt = t[1]-t[0] 
    ax.plot(U[0,:], U[1,:], label= T_S + "dt " + str(dt))
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title(T_S)
    ax.legend()
    
    if not Save:
        plt.show()

    else:
        ##Save Plots
        file = T_S + "_dt_" + str(dt) +".png"
        path = os.path.join(os.getcwd(), 'Plots')
        
        if not os.path.exists(path):
            os.makedirs(path)
        
        plt.savefig(os.path.join(path,file))
        
def Plot_CP_all(U,t, T_S, Save):
    fig, ax = plt.subplots(figsize=(10, 10))
    for i in t:
        dt = t[i][1]-t[i][0] 
        ax.plot(U[i][0,:], U[i][1,:], label= T_S + " dt " + str(dt))
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title(T_S)
    ax.legend()
    
    if not Save:
        plt.show()

    else:
        ##Save Plots
        file = T_S + ".png"
        path = os.path.join(os.getcwd(), 'Plots')
        
        if not os.path.exists(path):
            os.makedirs(path)
        
        plt.savefig(os.path.join(path,file)) 
       
    
    
    