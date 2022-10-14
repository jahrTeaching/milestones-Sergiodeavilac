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
    
    file = T_S + "_dt_" + str(dt) +".png"
    Save_plot(Save, file)
        
def Plot_CP_all(U,t, T_S, Save):
    fig, ax = plt.subplots(figsize=(10, 10))
    for i in t:
        dt = t[i][1]-t[i][0] 
        ax.plot(U[i][0,:], U[i][1,:], label= T_S + " dt " + str(dt))
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title(T_S)
    ax.legend()
    
    file = T_S + ".png"
    Save_plot(Save, file)

def Plot_Er(Er,t, dt, T_S, Save):
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.plot(t,Er[0,:], label= T_S + " dt " + str(dt))
    ax.plot(t, Er[1,:], label= T_S + " dt " + str(dt))
    ax.set_xlabel('t')
    ax.set_ylabel('Er')
    ax.set_title(T_S)
    ax.legend()
    
    file = T_S + "_dt_" + str(dt) +".png"
    Save_plot(Save, file)

def Plot_Er_compare(Er,t, dt, T_S, Save):
    fig, (ax, ay) = plt.subplots(2,1,figsize=(15, 15))
    for i in t:
        ax.plot(t[i],Er[i][0,:], label= T_S + " dt " + str(dt[int(i)]))
        ay.plot(t[i],Er[i][1,:], label= T_S + " dt " + str(dt[int(i)]))
    ax.set_xlabel('t')
    ax.set_ylabel('Er_x')
    ay.set_xlabel('t')
    ay.set_ylabel('Er_y')
    ax.set_title(T_S + ' Er')
    ax.legend()
    ay.legend()
    
    file = T_S + '_comprare' + ".png"
    Save_plot(Save, file)
    

def Plot_Conv_Rat(x,y, T_S, Save):
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.plot(x,y, label= T_S)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title(T_S)
    ax.legend()
    
    file = T_S + ".png"
    Save_plot(Save, file)
    
def Save_plot(Save, file):
    
    if not Save:
        plt.show()

    else:
        ##Save Plots
        
        path = os.path.join(os.getcwd(), 'Plots')
        
        if not os.path.exists(path):
            os.makedirs(path)
        
        plt.savefig(os.path.join(path,file)) 
    
    