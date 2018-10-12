#!/usr/bin/env python
import math

def circle(rad):
    return math.pi*pow(rad, 2)

def square(side):
    return pow(side, 2)
def add(x,y):
    return x + y

if __name__ == "__main__":
    print(circle(2))
    print(square(4))
    print(add(2,3))

