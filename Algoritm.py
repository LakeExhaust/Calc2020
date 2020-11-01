from Function import Function
import numpy;
class Algoritim:
    def __init__ (self, a, Function, guess):
        self.a = a
        self.Function = Function
        self.guess = guess;
        #Function for getting the best learning rate
    def newton(self):
        formula = (1/self.Function.f)
        print("Best learning rate is " + str(formula))
    def gradient (self):
            #Change + to get maximum
            formula = self.guess - self.a * self.Function.f
            print("Extrema:" +" "+ str(formula))











