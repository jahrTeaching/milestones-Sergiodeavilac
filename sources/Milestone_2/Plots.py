import matplotlib.pyplot as plt
import os


def Plot_CP (U,t,Nd, T_S):
    fig, ax = plt.subplots(figsize=(4, 4))
    dt = t[1]-t[0] 
    ax.plot(U[0,:], U[1,:], label= T_S + "dt " + str(dt))
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title(T_S)
    ax.legend()
    plt.show()
    
    ###Save Plots (Comment to not save) (Read Readme.txt for saving plots)
    # file = T_S + "_dt_" + str(dt) +".png"
    # path = os.path.join(os.path.dirname(os.path.abspath("Main_ML2.py")), 'Plots')
    
    # if not os.path.exists(path):
    #     os.makedirs(path)
    
    # plt.savefig(os.path.join(path,file))
    