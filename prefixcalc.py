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
__version__ = "0.1.0"

import sys
import os
from datetime import datetime
import logging
from logging import handlers
# BOILERPLATE
# TODO: usar função
# TODO: usar lib (loguru)
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("prefixcalc.py", log_level)
#ch = logging.StreamHandler()
#ch.setLevel(log_level)
fh = handlers.RotatingFileHandler(
    "prefixlog.log",
    maxBytes=10**6,
    backupCount=10,
)
fmt = logging.Formatter(
    '%(asctime)s  %(name)s  %(levelname)s '
    'l:%(lineno)d f:%(filename)s: %(message)s'
)
fh.setFormatter(fmt)
log.addHandler(fh)

arguments = sys.argv[1:]

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

valid_operations = ("sum", "sub", "mul", "div")
if operation not in valid_operations:
    print("Operação inválida.")
    print(valid_operations)
    sys.exit(1)

validated_nums = []
for num in nums:
    # TODO: Repetição while + exceptions
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

# TODO: Usar dict de funções
if operation == "sum":
    result = n1 + n2
elif operation == "sub":
    result = n1 - n2
elif operation == "mul":
    result = n1 * n2
elif operation == "div":
    result = n1 / n2

path = os.curdir
filepath = os.path.join(path, "prefixcalc.log")
timestamp = datetime.now().isoformat()
user = os.getenv("USER", "anonymous")

print(f"O Resultado é {result}")

try:
    with open(filepath, "a") as file_:
        file_.write(f"{timestamp} - {user} - {operation}, {n1}, {n2} = {result}\n")
except PermissionError as e:
    # TODO: logging
    log.error(
        '%(str(e))s'
    )
    sys.exit(1)

#print(f"{operation}, {n1}, {n2} = {result}", file=open(filename, "a"))



