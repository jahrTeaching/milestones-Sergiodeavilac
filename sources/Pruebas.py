from numpy import linspace
import matplotlib.pyplot as plt

    
    
def deco_plot(f):
    def f(a, b):
        
        x, y = f(a, b)
        
        fig, ax = plt.subplots()
        ax.plt(x,y)
        ax.grid()
        ax.show
        return f(a, b)
    return deco_plot(f)

def func(a,b):
    x = linspace(0,a,10)
    y = linspace(0,b,10)
    return x, y
        
if __name__ == "__main__":
    
    @deco_plot
    func(10,3)