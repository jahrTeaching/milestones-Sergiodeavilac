import matplotlib.pyplot as plt
from numpy import sqrt
import os

def Plot_CP(U,t, T, dt, T_S, Save):
    fig, ax = plt.subplots( figsize = (10, 10) )
    dt = t[1]-t[0] 
    ax.plot(U[0,:], U[1,:], label= T_S + "dt " + str(dt))
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title(T_S)
    ax.legend()
    
    file = T_S + "_dt_" + str(dt) +".png"
    Save_plot(Save, file)
        
def Plot_CP_all(U,t, T, dt, T_S, Save):
    fig, ax = plt.subplots( figsize=(10, 10) )
    colors = ['r','b','g']
    for i in t:
        ax.plot(U[i][0,:], U[i][1,:], color = colors[int(i)], label= T_S + " dt " + str(dt[int(i)]))
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title(T_S + ' compare dt for T = ' + str(T))
    ax.legend()
    
    file = T_S + ".png"
    Save_plot(Save, file)

def Plot_Er(Er,t, T, dt, T_S, Save):
    fig, ax = plt.subplots( figsize = (10, 10) )
    ax.plot(t, Er[0,:], color = 'b' , label = 'Er_x' )
    ax.plot(t, Er[1,:], color = 'r', label =  'Er_y' )
    ax.set_xlabel('t')
    ax.set_ylabel('Er')
    ax.set_title(T_S + ' dt = ' + str(dt) + ' T = ' + str(T) )
    ax.legend()
    
    file = T_S + "_dt_" + str(dt) + '_T_' + str(T)  +".png"
    Save_plot(Save, file)

def Plot_Er_compare(Er,t, T, dt, T_S, Save):
    fig, (ax, ay, az) = plt.subplots(3,1,figsize=(15, 15))
    colors = ['r','b','g']
    for i in t:
        Er_n = sqrt(Er[i][0,:]**2 + Er[i][1,:]**2)
        ax.plot(t[i],Er[i][0,:], color = colors[int(i)], label= T_S + " dt " + str(dt[int(i)]))
        ay.plot(t[i],Er[i][1,:], color = colors[int(i)], label= T_S + " dt " + str(dt[int(i)]))
        az.plot(t[i],Er_n, color = colors[int(i)], label = 'Norm' + " dt " + str(dt[int(i)]))
    ax.set_xlabel('t')
    ax.set_ylabel('Er_x')
    ay.set_xlabel('t')
    ay.set_ylabel('Er_y')
    az.set_xlabel('t')
    az.set_ylabel('Er_norm')
    ax.set_title(T_S + ' Er' + ' T = ' + str(T))
    ax.legend()
    ay.legend()
    az.legend()
    
    file = T_S + '_comprare_T' + str(T) + ".png"
    Save_plot(Save, file)
    
def Plot_Conv_Rat(x, y, T, dt, regress, T_S, Save):
    fig, ax = plt.subplots(figsize = (10, 10))
    ax.plot(x,y, color = 'b', label = 'Numerical results')
    ax.plot(x, regress.intercept + regress.slope*x, '--', color = 'r',  label = 'linear regression')
    ax.set_xlabel('Log_N')
    ax.set_ylabel('Log_Er')
    ax.set_title(T_S + ': T = ' + str(T) +', dt = ' + str(dt) + '. R^2 = ' + str(round(regress.rvalue**2,3)) + ' & Order = ' + str(round(abs(regress.slope),3)))
    ax.legend()
    
    file = T_S +'_dt_'+ str(dt) +'_conver' + ".png"
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
    
    