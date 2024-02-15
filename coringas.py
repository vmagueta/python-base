
# Solid - Single Responsibility
def funcao(*args, timeout=10, **kwargs):
    for item in args:
        print(item)

    print(kwargs)
    
    print(f"timeout {timeout}")

funcao(
    "Bruno",
    1,
    True,
    [],
    timeout=90,
    nome = "joao", 
    cidade="viana", 
    data="hoje",
    banana=1,
    panela=3,
    teclado=True,
)
