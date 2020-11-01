import math


class Function:
    def __init__(self, x, f):
        self.f = f;
        self.x = x;

    def get_f (self):
        print("Result of f'(x) " + " : " +  str(self.f))
        return self.f

    def set_f (self, x):
        self.f = x

    def set_x (self, x):
        self.x = x

