import matplotlib.pyplot as plt
import os


def Plot_CP (U,t, T_S, Save):
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
        path = os.path.join(os.path.dirname(os.path.abspath("Main_ML2.py")), 'Plots')
        
        if not os.path.exists(path):
            os.makedirs(path)
        
        plt.savefig(os.path.join(path,file))
        
    
    
    