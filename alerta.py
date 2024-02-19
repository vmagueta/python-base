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

log = logging.Logger("alerta")

# TODO: Mover para módulo de utilidades.

def is_completely_filled(dict_of_inputs):
    """Returns a boolean telling if a dict is completely filled."""
    info_size = len(dict_of_inputs)
    filled_size = len(
        [value for value in dict_of_inputs.values() if value is not None]
    )
    return info_size == filled_size


def read_inputs_for_dict(dict_of_info):
    """Reads information for a dict from user input."""
    for key in dict_of_info.keys(): # ["temperatura", "umidade"]
        if dict_of_info[key] is not None:
            continue
        try:
            dict_of_info[key] = int(input(f"{key}: "))
        except ValueError:
            log.error("%s inválidade, digite números", key)
            break # para o for


# PROGRAMA PRINCIPAL

info = {"temperatura": None, "umidade": None}

while not is_completely_filled(info):
    read_inputs_for_dict(info)

temp, umidade = info.values() # unpacking [30, 90]

if temp > 45:
    print("ALERTA!!! 🥵 Perigo, calor extremo.")
elif temp > 30 and temp * 3  >= umidade:
    print("ALERTA!!! 🥵🌊 Perigo de calor úmido.")
elif temp >= 10 and temp <= 30: # elif temp in range(10, 31):
    print("😃 Normal")
elif temp >= 0 and temp < 10:
    print("🥶 Frio")
elif temp < 0:
    print("ALERTA!!! ☃️ Frio extremo.")
