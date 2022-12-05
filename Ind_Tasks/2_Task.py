#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import sys

if __name__ == '__main__':
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    if a == 0:
        print("Ошибка!", file=sys.stderr)
        exit(1)
    else:
        D = b * b + 4 * a * c
        if D > 0:
            t1 = (-b + D) / (2 * a)
            t2 = (-b + (-D)) / (2 * a)
            if t1 >= 0:
                x1 = math.sqrt(t1)
                x2 = -math.sqrt(t1)
                print(f"x1={x1}, x2={x2}")
            if t2 >= 0:
                x3 = math.sqrt(t2)
                x4 = -math.sqrt(t2)
                print(f"x3={x3}. x4={x4}")
            else:
                print("Действительных корней нет")
        elif D == 0:
            t1 = -b / (2 * a)
            if t1 >= 0:
                x1 = math.sqrt(t1)
                x2 = -math.sqrt(t1)
                print(f"x1={x1}, x2={x2}")
            else:
                print("Действительных корней нет")
        elif D < 0:
            print("Действительных корней нет")
