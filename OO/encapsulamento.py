# Encapsulamento: Capacidade de esconder/proteger atributos
#                 dentro da classe publico, protegidas, privadas


# # Convenção de nomes
class Conta:
    _tipo_de_conta = "corrente" # protegido / protected
    __id_interno = 456789  # atributo privado / caiu em desuso

    def __init__(self, cliente):
        self.cliente = cliente
        self._saldo = 0  # protegido


    def depositar(self, value):  # setter - set_saldo
        self._saldo += value


    def sacar(self, value):
        if self._saldo < value:
            print("AVISO: Saldo insuficiente")
            return
        self._saldo -= value


    def consultar(self):  # getter - get_saldo
        if self._saldo < 0:
            print("AVISO: Você está devendo...")
        return self._saldo


conta = Conta("Bruno")
# print(conta._saldo)  Code Smell - estar em uma instância e acessar um _atributo
print(conta.consultar())

# conta._saldo = 100  Code Smell
conta.depositar(100)
conta.depositar(50)
print(conta.consultar())
conta.sacar(80)
print(conta.consultar())
conta.sacar(200)
print(conta.consultar())


# # Propriedades
from abc import ABC

class Conta(ABC):
    def __init__(self, cliente):
        self.cliente = cliente
        self._saldo = 0

class ContaCorrente(Conta):
    _id_interno = 456789

    @property  # Não precisa mais passar como conta.saldo()
    def saldo(self):
        if self._saldo < 0:
            print("AVISO: Você está devendo...")
        return self._saldo

    @saldo.setter  # Não é obrigado a criar em caso de ter @property
    def saldo(self, value):
        self._saldo += value


    @saldo.deleter  # Não é obrigado a criar em caso de ter @property
    def saldo(self):
        self._saldo = 0

conta = ContaCorrente("Bruno")
print(conta.cliente)
print(conta.saldo)

# depositos
conta.saldo = 100
print(conta.saldo)
conta.saldo = 200
print(conta.saldo)

# saque
conta.saldo = -50
print(conta.saldo)

#reiniciar a conta
del conta.saldo
print(conta.saldo)
