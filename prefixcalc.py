#! usr/bin/env python3
"""Calculadora Prefix.

Funcionamento:

[operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ prefixcalc.py sum 5 2
7

$ prefixcalc.py mul 10 5
50

$ prefixcalc.py 
operação: sum
n1: 5
n2: 4
9

Os resultados serão salvos em 'prefixcalc.log'
"""
__version__ = "0.1.1"

import sys
import os
from datetime import datetime
# BOILERPLATE
# TODO: usar lib (loguru)

arguments = sys.argv[1:]

valid_operations = {
    "sum": lambda n1, n2: n1 + n2,
    "sub": lambda n1, n2: n1 - n2,
    "mul": lambda n1, n2: n1 * n2,
    "div": lambda n1, n2: n1 / n2,
}

path = os.curdir
filepath = os.path.join(path, "prefixcalc.log")
timestamp = datetime.now().isoformat()
user = os.getenv("USER", "anonymous")

while True:

    if not arguments:
        operation = input("operação: \n")
        n1 = input("n1: \n")
        n2 = input("n2: \n")
        arguments = [operation, n1, n2]
        
    elif len(arguments) != 3:
        print("Número de argumentos inválidos.")
        print("ex: sum 5 5")
        sys.exit(1)
    
    operation, *nums = arguments

    if operation not in valid_operations:
        print("Operação inválida.")
        print(valid_operations)
        sys.exit(1)
    
    validated_nums = []
    for num in nums:
        if not num.replace(".", "").isdigit():
            print(f"Número inválido {num}")
            sys.exit(1)
        if "." in num:
            num = float(num)
        else:
            num = int(num)
        validated_nums.append(num) 
    try:
        n1, n2 = validated_nums
    except ValueError as e:
        print(str(e))
        sys.ext(1)

    result = valid_operations[f"{operation}"](n1,n2)
    
    print(f"O Resultado é {result}")
    
    try:
        with open(filepath, "a") as log:
            log.write(
            f"{timestamp} - {user} - {operation}, {n1}, {n2} = {result}\n"
            )
    except PermissionError as e:
        log.error(
            '%(str(e))s'
        )
        sys.exit(1)
    
    #print(f"{operation}, {n1}, {n2} = {result}", file=open(filename, "a"))

    arguments = None

    if input("Pressione enter para continuar ou qualquer tecla para sair\n"):
        break
