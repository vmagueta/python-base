

import sys
import os
import smtplib
from email.mime.text import MIMEText

arguments = sys.argv[1:]
if not arguments:
    print("Informe o nome do arquivo de e-mails")
    sys.exit(1)
    
filename = arguments[0]
templatename = arguments[1]

path = os.curdir
filepath = os.path.join(path, filename) # emails.txt
templatepath = os.path.join(path, templatename) # email_tmpl.txt

with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
    server.login(user="vmagueta7@gmail.com", password="magueta07")
        
    for line in open(filepath):
        name, email = line.split(",")
        text = (
            open(templatepath).read()
            %{
                "nome": name,
                "produto":"caneta",
                "texto":"Escrever muito bem",
                "link":"https://canetaslegais.com",
                "quantidade":1,
                "preco":50.5,
            }
        )

        from_ = "vmagueta7@gmail.com"
        to = ", ".join([email])
        
        message = MIMEText(text)
        message["Subject"] = "Compre mais"
        message["From"] = from_
        message["To"] = to

        server.sendmail(from_, to, message.as_string())
