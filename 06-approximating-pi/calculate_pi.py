import numpy as np
import matplotlib.pyplot as plt

def calculate_pi(total):
    inside=0
    
    x_inside=[]
    x_outside=[]
    y_inside=[]
    y_outside=[]

    for i in range(0,total):
        nx=np.random.random()
        ny=np.random.random()
    
        if nx**2 + ny**2 <=1:
            inside = inside + 1
            x_inside.append(nx)
            y_inside.append(ny)
        else:
            x_outside.append(nx)
            y_outside.append(ny)

#print(inside)

    plt.scatter(x_inside, y_inside, c='red',s=0.25)
    plt.scatter(x_outside, y_outside, c='blue',s=0.25)
    
    plt.show()

    pi=4*(inside/total)
    return pi
