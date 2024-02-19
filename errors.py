#! usr/bin/env python3

import sys
import os
import time
import logging

log = logging.Logger("errors")

# EAFP - Easy to Ask forgiveness than permission
# (É mais fácil pedir perdão, do que permissão)

def try_to_open_a_file(filepath, retry=1) -> list:
    """ tries to open a file, if error, retries n times"""
    if retry > 999:
        raise ValueError("Retry cannot be above 999")
    try:
        return open(filepath).readlines() # FileNotFoundError
    except (FileNotFoundError, ZeroDivisionError) as e: 
        log.error("ERRO: %s", e)
        time.sleep(2)
        if retry > 1:
            # recursão (só até 1000 vezes)
            return try_to_open_a_file(filepath, retry=retry - 1) # DEADLOCK
    else:
        print("Sucesso!")
    finally:
        print("Execute isso sempre!!")
    return[]


for line in try_to_open_a_file("names.txt", retry=5):
    print(line)
