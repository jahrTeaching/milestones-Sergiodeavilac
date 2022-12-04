from numpy import linspace
import matplotlib.pyplot as plt

import multiprocessing as mp

def func():
    i = 0
    while i < 1e20:
        i += 1
        
    return i

# Step 1: Init multiprocessing.Pool()
pool = mp.Pool(mp.cpu_count())

# Step 2: `pool.apply` the `howmany_within_range()`
results = [pool.apply(func, args=())]

# Step 3: Don't forget to close
pool.close()    

print(results)
    
# def deco_plot(f):
#     def f(a, b):
        
#         x, y = f(a, b)
        
#         fig, ax = plt.subplots()
#         ax.plt(x,y)
#         ax.grid()
#         ax.show
#         return f(a, b)
#     return deco_plot(f)

# def func(a,b):
#     x = linspace(0,a,10)
#     y = linspace(0,b,10)
#     return x, y
        
# if __name__ == "__main__":
    
#     @deco_plot
#     func(10,3)