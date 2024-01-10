#! usr/bin/env python3
"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala
que frequentam cada uma das atividades.
"""
__version__ = "0.1.2"

# Dados
aulas = {
    "Inglês": {
        "sala1": ["Erik","Maia","Joana"],
        "sala2": ["Carlos","Antonio"]
    },
    "Música" : {
        "sala1": ["Erik"],
        "sala2": ["Carlos", "Maria"]
    },
    "Dança" : {
        "sala1": ["Gustavo","Sofia", "Joana"],
        "sala2": ["Antonio"]
    }
}

# Listar alunos em cada atividade por sala
for aula,sala in aulas.items():

    print(f"Alunos da atividade de: {aula}")
    print("-" * 28)
    for nome_da_sala, alunos in sala.items():
        print(f"Alunos da sala {nome_da_sala}")
        for aluno in alunos:
            print(f" {aluno}") 
