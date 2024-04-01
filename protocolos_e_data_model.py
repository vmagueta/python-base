# Protocolos / Data Model
# Printable
# Addible - __add__ / __radd__

class Cor:  # Base Class

    def explode(self):
        return "💣💣💣💣💣💣"

    def __str__(self):
        return self.icon

    def __add__(self, other):
        mixtable = [
            ((Amarelo, Vermelho), Laranja),
            ((Azul, Amarelo), Verde),
            ((Vermelho, Azul), Violeta),
        ]
        for mix, result in mixtable:
            if isinstance(self, mix) and isinstance(other, mix):
                return result()


class Amarelo(Cor):
    icon = "🟨"


class Azul(Cor):
    icon = "🟦"

    def __len__(self):
        return 3


class Vermelho(Cor):
    icon = "🟥"

    def __len__(self):
        return 1


class Laranja(Cor):
    icon = "🟧"


class Verde(Cor):
    icon = "🟩"

    def __len__(self):
        return 2


class Violeta(Cor):
    icon = "🟪"


amarelo = Amarelo()
azul = Azul()
vermelho = Vermelho()

print("Cores primárias:")
print(amarelo, azul, vermelho)
print()

print("Cores Secundárias:")
print("Amarelo + Vermelho = ", amarelo + vermelho)
print("Azul + Amarelo", azul + amarelo)
print("Vermelho + Azul = ", vermelho + azul)
print()


# Iterable - __iter__
# Container - __contains__ -> bool
class Paleta:
    def __init__(self, *cores):
        self._cores = cores

    def __len__(self):
        return len(self._cores)

    def __iter__(self):
        return iter([cor.icon for cor in self._cores])

    def __contains__(self, item):
        return item in [cor.icon for cor in self._cores]

    def __getitem__(self, item):
        if isinstance(item, (int, slice)):  # 0, 2:4
            return self._cores[item]
        if isinstance(item, str):
            for cor in self._cores:
                if cor.__class__.__name__.lower() == item.lower():
                    return cor


rgb = Paleta(Vermelho(), Verde(), Azul())

print("Cores RGB")
for cor in rgb:
    print(cor)

print("🟥" in rgb)
print()


# Sized
print(len(rgb))
print()


# Collection - Sized + Container + Iterable - (Junta os 3 protocolos)


# Subscripable
print(rgb[0])
print(rgb["verde"])
print(rgb[-1])


# Podemos criar nossos próprios protocolos
def explode_color(color):  # Explodable
    if not hasattr(color, 'explode'):
        raise TypeError("Color is not Explodable")
    print(color, "-->", color.explode())


explode_color(Vermelho())


# protocolos padrões
class Thing():
    def __getattribute__(self, __name: str):
        return "default"


t = Thing()
print(t)

t.valor = 10
print(t.valor)

del t.valor
print(t.valor)

print(t.banana)

# __new__               = Construtor chamado antes de criar a instância
# __init__              = Inicializador chamado após a instância ser criada
# __init_subclass__     = Inicializador de subclases
# __repr__              = Imprime a representação em string
# __str__               = chama __repr__ por padrão
# __setattr__           = executado sempre que atribuimos com `obj.name = `
# __getattr__           = executado quando acessamos `obj.name`
# __delattr__           = executado quandos apagamos com `del obj.name`
# __getattribute__      = executado quando um atributo não é encontrado
# __dir__               = lista todos os atributos e métodos
