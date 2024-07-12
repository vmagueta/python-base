from dataclasses import dataclass

@dataclass
class Pessoa:
    pk: str
    name: str
    points: int = 100  # Passar valor default é possível

def funcao(dados: Pessoa):
    ...


dados = Pessoa(pk="joe@doe.com", name="Joe", points=10)

print(dados.name)

funcao(dados)

########################################

def imprime_mensagem(msg: int | str | list | float | None = None):
    print(msg)  # Printable  -  __str__

imprime_mensagem("Bruno")
imprime_mensagem(123)
imprime_mensagem([1, 2, 3])
imprime_mensagem(5.6)


#######################################

# Carrinho de compras
from decimal import Decimal

# Usar em:
# ass função
# def classe
# métodos

# Não anotar o tipo em variáveis, já está claro!
produto = "Caneta"
# valor = 4.5  float
valor = Decimal(4.5)
quantidade = 5
cliente_especial = True


# Interessante sempre anotar o tipo em funções!
def calcula_total(valor: Decimal, quantidade: int) -> Decimal:
    return valor * quantidade

if cliente_especial:
    valor = Decimal(4.3)  # BUG  / float


total = calcula_total(valor, quantidade)

print("Tipo:", type(total))
print(f"O total é R$ {total:.2f}")
