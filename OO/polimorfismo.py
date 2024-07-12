# Polimorfismo: Capacidade de uma implementação se comportar
# de maneira similar independente da forma do objetop

class Dog:
    def make_sound(self):
        return "woof woof"


class Cat:
    def make_sound(self):
        return "meow meow"


class Guitar:
    def make_sound(self):
        return "inheininheim"


def print_sound(obj):  # 'Soundable'
    if not hasattr(obj, "make_sound"):
        raise TypeError(f"{obj} is not Soudable")
    print(obj.make_sound())  # implementa make_sound


rex = Dog()
print_sound(rex)

lili = Cat()
print_sound(lili)

print_sound(Guitar())

# print_sound(42)  Não implementa o 'make_sound', não é 'Soundable'


# Duck Typing
"""
Se o objeto anda como um pato,
parece um pato, faz quack como um pato,
então é um pato!
"""

def funcao(*args): # (a, b, c)
#    return a + b + c  Não polimorfico
    ret = 0
    for arg in args:
        ret += arg
    return ret

print(funcao(1, 2, 3))

print(funcao(1, 2, 3, 4))

print(funcao(1, 2, 3, 4, 5))
print(funcao())
