#! usr/bin/env python3
"""Exemplos de envio de e-mail"""
import smtplib

SERVER = "localhost"
PORT = 8025



FROM = "vmagueta7@gmail.com"
TO = ["victormagueta7@gmail.com", "kamilamagueta@gmail.com"]
SUBJECT = "Meu e-mail via Python"
TEXT = """\
Este é o meu primeiro e-mail enviado pelo Python.
<b>Olá Mundo</b>
"""

# SMTP
message = f"""\
From: {FROM}
To: {", ".join(TO)}
Subject: {SUBJECT}

{TEXT}
"""

with smtplib.SMTP(host=SERVER, port=PORT) as server:
    server.sendmail(FROM, TO, message.encode("utf-8"))
