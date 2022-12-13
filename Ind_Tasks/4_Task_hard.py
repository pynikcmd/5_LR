#!\usr\bin\env python3
# -*- coding: utf-8 -*-

import sys
import math

# Постоянная Эйлера.
EULER = 0.5772156649015328606
# Точность вычислений.
EPS = 1e-10

if __name__ == '__main__':
    x = float(input("Value of x: "))
    if x == 0:
        print("Illegal value of x", file=sys.stderr)
        exit(1)
    a = x
    S, n = a, 1
    while math.fabs(a) > EPS:
        a *= (2*n) / ((2*n + 2)**2) * (2*n + 1)
        S += a
        n += 1
    print(f"Chi({x}) = {EULER + math.log(math.fabs(x)) + S}")
