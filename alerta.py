#! usr/bin/env python3
"""
Alarme de Temperatura

Faça um script que pergunta ao usuário qual a temperatura atual e o indice de
umidade do ar, sendo que caso será exibida uma mensagem de alerta dependendo
das condições:

temp maior que 45: ALERTA!!! Perigo, calor extremo;
temp vezes 3 for maior ou igual a umidade: ALERTA!! Perigo de calor úmido;
temp entre 10 e 30: Normal
temp entre 0 e 10: Frio
temp <0: ALERTA!!! Frio extremo
"""

import logging
import sys

log = logging.Logger("ALERTA")
ch = logging.StreamHandler()
fmt = logging.Formatter(
    '%(levelname)s\n'
    '%(asctime)s \n'
    'file: %(filename)s line: %(lineno)d \n'
    'message: %(message)s'
)
ch.setFormatter(fmt)
log.addHandler(ch)

info = {
    "temperatura": None,
    "umidade": None
}
keys = info.keys()

for key in keys:
    try:
        info[key] = float(input(f"Qual a {key}? \n").strip())
         
    except ValueError:
        log.error(f"{key.capitalize()} inválida")
        sys.exit(1)

temp = info["temperatura"]
umid = info["umidade"] 
umid_alert = info["temperatura"] * 3

if temp > 45:
    print("ALERTA!!! Perigo, calor extremo.")
elif umid <= umid_alert:
    print("ALERTA!!! Perigo de calor úmido.")
elif temp >= 10 and temp <= 30: # elif temp in range(10, 31):
    print("Normal")
elif temp >= 0 and temp < 10:
    print("Frio")
elif temp < 0:
    print("ALERTA!!! Frio extremo.")
