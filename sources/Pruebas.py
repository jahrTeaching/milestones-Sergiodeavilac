import matplotlib.pyplot as plt
from numpy import linspace
def prueba(func):
    def wrapped_func(*args, **kwargs):
        
        x,y = func(*args, **kwargs)
        fig, ax = plt.subplots()
        ax.plot(x,y)
        plt.show()
        
        return func(*args, **kwargs)
    return wrapped_func
    
@prueba
def f(a,b):
    x = linspace(0,a,10)
    y = linspace(0,b,10)
    return x, y




if __name__ == '__main__':
    f(5,5)
    