#!/usr/bin/env python
import math

def circle(rad):
    return math.pi*pow(rad, 2)

def square(side):
    return pow(side, 2)

if __name__ == "__main__":
    print(circle(2))
    print(square(4))

