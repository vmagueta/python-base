# Abstração: Capacidade de abstrair implementações
# Herança: Capacidade de herdar de outras classes
# Polimorfismo: Capacidade de uma implementação
#               se comportar de maneira similar
#               independente da forma do objeto
# Encapsulamento: Capacidade de esconder/proteger
#                 atributos dentro da classes
#                 publico, protegidas, privadas
# # Propriedades
from abc import ABC


class Conta(ABC):
    def __init__(self, cliente):
        self.cliente = cliente
        self._saldo = 0  # protegido


class ContaCorrente(Conta):
    _id_interno = 546789

    @property  # getter
    def saldo(self):
        if self._saldo < 0:
            print("AVISO: Você está devendo.")
        return self._saldo

    @saldo.setter
    def saldo(self, value):
        self._saldo += value

    @saldo.deleter
    def saldo(self):
        self._saldo = 0


conta = ContaCorrente("Bruno")
print(conta.cliente)
print(conta.saldo)

# depósitos
conta.saldo = 100
print(conta.saldo)

conta.saldo = 200
print(conta.saldo)

# saque
conta.saldo = -50
print(conta.saldo)

# reiniciar a conta
del conta.saldo
print(conta.saldo)
