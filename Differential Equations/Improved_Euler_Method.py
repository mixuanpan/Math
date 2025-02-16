'''
Example Question: 

Use the improved Euler method with a computer system to find the desired solution value. 
Start with step size h = 0.1, and then successively smaller step sizes until successive approximate solutions at x = 2 agree rounded off to four decimal places.

'''

import math 
import numpy as np

y = 0 # starting value for y 
x = 0 # starting value for x; using the interval [0, 2] in this example 
h = [0.1, 0.01, 0.001, 0.0001] # step sizes 

for i in h:
    for j in np.arange(0, 2, i): # use np.arange to easily loop with decimal increments 
        # dy / dx is given in this example 
        y += i * (pow(x, 2) + 3 * pow(y, 2) - 7) # (step size) * (dy / dx) 
        x += i
    print("The approximation when h = ", i, " is ", y)
    # reset the values of x and y for the next step size 
    x = 0 
    y = 0

# compare the result of each step for the decimal places 
# as long as the function is not periodic, the approximation with the less step size should be more accurate, given the more number of accurate decimal places
