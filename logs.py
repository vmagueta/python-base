#!/usr/bin/env python3

import os
import logging
from logging import handlers

# BOILERPLATE
# TODO: Mover para um módulo de utilidades
# TODO: usar lib (loguru)
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("logs.py", log_level)
#ch = logging.StreamHandler() # Console/terminal/stderr
#ch.setLevel(log_level)
fh = handlers.RotatingFileHandler(
    "meulog.log",
     maxBytes=300, #10**6
     backupCount=10,
)
fh.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s  %(name)s  %(levelname)s '
    'l:%(lineno)d f:%(filename)s: %(message)s'
)
fh.setFormatter(fmt)
log.addHandler(fh)

"""
log.debug("Mensagem pro dev, qe, sysadmin")
log.info("Mensagem geral para usuários")
log.warning("Aviso que não causa erro")
log.error("Erro que afeta uma única execução")
log.critical("Erro geral ex: banco de dados sumiu")
"""

print("---")

try:
    1 / 0

except ZeroDivisionError as e:
    log.error("Deu erro %s", str(e))
