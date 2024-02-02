#! usr/bin/env python3
"""
Repete vogais

Faça um programa que pede ao usuário que digite uma ou mais palavras
e imprime cada uma das palavra com as suas vogais duplicadas.

ex:
python repete_vogal.py
'Digite uma palavra (ou enter para sair): Python'
'Digite uma palavra (ou enter para sair): Bruno'
'Digite uma palavra (ou enter para sair): <enter>'

Pythoon
Bruunoo
"""

palavras = []
vogais = ("aeiouãáêéíõóú")


while True:
    palavra = input("Digite uma palavra (ou enter para sair): ").strip()

    nova_palavra = ""
    if not palavra:
        break

    for letra in palavra:
        # TODO: Remover acentuação usando função
        if letra.lower() in vogais:
            nova_palavra += letra * 2
        else:
            nova_palavra += letra
            
        # if ternário alternativo
        #nova_palavra += (
        #    letra * 2
        #    if letra.lower() in vogais
        #    else letra
        #)
        
    palavras.append(nova_palavra)

print(*palavras, sep="\n")
