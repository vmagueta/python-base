#! usr/bin/env python3
"""Bloco de notas.

Uso:
$ notes.py new "Minha Nota"
tag: tech
text: 
Anotação geral sobre carreira de tecnologia

$ notes.py read --tag=tech
...
...
"""
__version__ = "0.1.0"

import os
import sys

cmds = ("read", "new")
path = os.curdir
filepath = os.path.join(path, "notes.txt")

arguments = sys.argv[1:]

if not arguments:
    print("Invalid usage")
    print(f"You must specify subcommand: \n{cmds}")
    sys.exit()

if arguments[0] not in cmds:
    print(f"Invalid command '{arguments[0]}' ")

if arguments [0] == "read":
    try:
        for line in open(filepath):
            title, tag, text = line.split("\t")
            if tag.lower() == arguments[1].lower():
                print(f"title: {title}")
                print(f"text: {text}")
                print("-" * 30)
                print()
    except IndexError as e:
        print(str(e))
        print("You must specify the tag/subject you want me to read")
        print("Example: read 'tech'")
        sys.exit(1)

if arguments [0] == "new":
    try:
        title = arguments[1] # TODO: Tratar exception
        text = [
            f"{title}",
            input("tag: ").strip(),
            input("text: \n").strip(),
        ]
    except IndexError as e:
        print(str(e))
        print(f"[Error] You must write a Title before the command")
        print("Example: new 'title'")
        sys.exit(1)
    # \t - tsv
    with open(filepath, "a") as file_:
        file_.writelines("\t".join(text) + "\n")

