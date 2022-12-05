#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    count = 0
    for i in range(100, 1000):
        a = i % 10
        b = (i % 100) // 10
        c = i // 100
        suma = a + b + c
        if suma % 7 == 0 and i % 7 == 0:
            count += 1
        else:
            continue
    print(
        f"Сумма цифр трехзначного числа кратна 7.
        Само число также делится на 7. Таких чисел: {count}")
