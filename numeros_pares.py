#! usr/bin/env python3
"""
Faça um programa que imprime os números pares de 1 a 200

ex.
'python numeros_pares.py'
2
4
6
7
...
"""

for number in range(1,201):
    if number % 2 != 0:
        continue
    elif number % 2 == 0:
        print(number)
        number += 1
