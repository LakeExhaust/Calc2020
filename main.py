import math
import numpy as np
from Function import Function
from Algoritm import Algoritim
class DisplayInfo:
    #Guess by chaging x
    # Stored as floating

    x =  -1

    #First Derative
    expr = (5 * math.exp(math.pow(x, 2) / 8) * math.pi * math.sin(2 * math.pi * x) * math.exp(math.cos(2 * math.pi * x) / 2));
    #Second Derative
    expr2 = (5 * math.exp(math.pow(x, 2) / 8) - (5 * math.pow(x, 2) * math.exp(math.pow(x, 2) / 8) / 4) + (2 * math.pow(math.pi, 2) * math.cos(2 * math.pi * x) * math.exp(math.cos(2 * math.pi * x) / 2) - math.pow(math.pi, 2) * math.pow(math.sin(2 * math.pi * x), 2) * math.exp(math.cos(2 * math.pi * x) / 2)))

    #Will calculate the function at a certain point
    func = Function(x, expr2);
    func.get_f()
    #Gradient Descent Algoritm
    algo = Algoritim(0.026635092775, func, x)
    algo.gradient()
    #Will Caculate the best learning rate to use
    algo.newton()

