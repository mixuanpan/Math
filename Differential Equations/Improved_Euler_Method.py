'''
Example Question: 

Use the improved Euler method with a computer system to find the desired solution value. 
Start with step size h = 0.1, and then successively smaller step sizes until successive approximate solutions at x = 2 agree rounded off to four decimal places.

'''

import math 
import numpy as np

y = 0
x = 0
h = [0.1, 0.01, 0.001, 0.0001]

for i in h:
    for j in np.arange(0, 2, i):
        y += i * (pow(x, 2) + 3 * pow(y, 2) - 7)
        x += i
    print("The approximation when h = ", i, " is ", y)
    x = 0
    y = 0
