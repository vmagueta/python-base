#  Protocolos / Data Model


# # PRINTABLE
class Cor:  # Base Class
    english_name = "color"
    icon = "⬜"

    def __str__(self):
        return f"{self.english_name} - {self.icon}"


class Amarelo(Cor):
    icon = "🟨"
    english_name = "yellow"


class Azul(Cor):
    icon = "🟦"
    english_name = "blue"


class Vermelho(Cor):
    icon = "🟥"
    english_name = "red"


print("Cores Primárias")
obj = Amarelo()

new = str(obj)  # casting
print(new)

print(obj)
print(Azul())
print(Vermelho())



# # ADDIBLE - __add__ (atua no obj da esquerda) / __radd__ (atua no obj da direita)
# print (1 + 2)
print(1 .__add__(2))  # é o que acontece na expressão de cima
print("Bruno" + "Rocha")
print([1, 2, 3] + [4, 5, 6])


class Cor:
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


class Vermelho(Cor):
    icon = "🟥"


class Laranja(Cor):
    icon = "🟧"


class Verde(Cor):
    icon = "🟩"


class Violeta(Cor):
    icon = "🟪"


print("Cores Primárias")
amarelo = Amarelo()
azul = Azul()
vermelho = Vermelho()

print(amarelo, azul, vermelho)

print("Cores Secundárias")
print("Amarelo + Vermelho", amarelo + vermelho)  # Tipagem Forte
print("Azul + Amarelo", azul + amarelo)
print("Vermelha + Azul", vermelho + azul)



# # ITERABLE
class Cor:
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


class Vermelho(Cor):
    icon = "🟥"


class Laranja(Cor):
    icon = "🟧"


class Verde(Cor):
    icon = "🟩"


class Violeta(Cor):
    icon = "🟪"


class Paleta:
    def __init__(self, *cores):
        self._cores = cores

    def __iter__(self):
        return iter([cor for cor in self._cores])



rgb = Paleta(Vermelho(), Verde(), Azul())

for cor in rgb:
    print(cor)




# # CONTAINER  -  __ contains__ -> bool
class Cor:
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


class Vermelho(Cor):
    icon = "🟥"


class Laranja(Cor):
    icon = "🟧"


class Verde(Cor):
    icon = "🟩"


class Violeta(Cor):
    icon = "🟪"


class Paleta:
    def __init__(self, *cores):
        self._cores = cores

    def __iter__(self):
        return iter([cor for cor in self._cores])

    def __contains__(self, item):
        return item in [cor.icon for cor in self._cores]


rgb = Paleta(Vermelho(), Verde(), Azul())
print("🟦" in rgb)



# # SIZED
class Cor:
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



# # COLLECTION - Mistura Sized, Containers e Itarables
# A paleta é uma COLLECTION, pois implementa os três protocolos
class Paleta:
    def __init__(self, *cores):
        self._cores = cores

    def __len__(self):
        return len(self._cores)

    def __iter__(self):
        return iter([cor for cor in self._cores])

    def __contains__(self, item):
        return item in [cor.icon for cor in self._cores]


rgb = Paleta(Vermelho(), Verde(), Azul())

for cor in rgb:
    print(cor, len(cor))
print(len(rgb))



# # SUBSCRIPTABLE  -  __getitem__
class Cor:
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


class Paleta:
    def __init__(self, *cores):
        self._cores = cores

    def __len__(self):
        return len(self._cores)

    def __iter__(self):
        return iter([cor for cor in self._cores])

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
print(rgb[0])
print(rgb[-2])
print(rgb["azul"])



# # INTERFACE (Nominal)
class Cor:

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


class Paleta:
    def __init__(self, *cores):
        self._cores = cores

    def __len__(self):
        return len(self._cores)

    def __iter__(self):
        return iter([cor for cor in self._cores])

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


def explode_color(color):  # Explodable
    if not hasattr(color, 'explode'):
        raise TypeError("Color is not Explodable")
    print(color.explode())

explode_color(Vermelho())



# # PROTOCOLOS DEFAULT
class Thing:
    ...

t = Thing() # __new__  / __init__  /  __init_subclass__
print(t)  # __str__  /  __repr__

t.valor = 10  #  __setattr__
print(t.valor)  # __getattr__

del t.valor  # __delattr__
print(t.valor)  # __getatribute__  (Chamado quanto o atributo não é encontrado no obj)

print(dir(t))  # __dir___



# __new__              # Construtor chamado antes de criar a intância
# __init__             # Inicializador chamado após a instância é criada
# __init_subclass__    # Inicializador de subclasses
# __repr__             # Imprime a representação em string
# __str__              # chama __repr__ por padrão
# __setattr__          # executado sempre que atribuimos com obj.name = value
# __getattr__          # executado quando acessamos obj.name
# __delattr__          # executado quando apagamos com `del obj.name`
# __getattribute__     # executado quando um atributo não é encontrado
# __dir__              # lista todos os atributos e métodos
