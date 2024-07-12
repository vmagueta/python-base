# Henrança: Capacidade de abstrair implementações
# Abstração: Capacidade de herdar de outras classes

# super classe
class Fruit:  # Classe Abstrata / base
    kingdom = "vegetalia"


# derivadas (sub classe)

class Apple(Fruit):  # Herança em uma classe material
    internal_color = "white"


class RedApple(Apple):
    external_color = "red"


class GreenApple(Apple):
    external_color = "green"


class MinhaMacaQueEstaEmCimaDaMesa(GreenApple):
    ...


minha_maca = MinhaMacaQueEstaEmCimaDaMesa()
print(minha_maca.external_color)
print(minha_maca.internal_color)
print(minha_maca.kingdom)



# Forma mais fácil de manter e código mais limpo



class Fruit:  # Classe Abstrata / base
    kingdom = "vegetalia"

    def __init__(self, colors):
        self.colors = colors


# derivadas (sub classe)

class Apple(Fruit):  # Herança em uma classe material
    image = "🍎"


minha_maca = Apple(colors=["green", "white"])
print(minha_maca.colors)
print(minha_maca.kingdom)
print(minha_maca.image)


class Watermelon(Fruit):
    image = "🍉"


minha_melancia = Watermelon(colors=["green", "red", "black"])
print(minha_melancia.colors)
print(minha_melancia.image)


### Mixins

from abc import ABC  # Abstract Base Class


# super classe
class Fruit(ABC):  # Classe Abstrata / base
    kingdom = "vegetalia"

    def __init__(self, colors):
        self.colors = colors


class Food(ABC):
    price = 4.5


# derivadas (sub classe)

class Radioative(ABC):
    power = 100

class Apple(Fruit, Food, Radioative):  # Mixins
    image = "🍎"


fruta = Apple(colors=["black"])
print(id(fruta))
print(fruta.colors, fruta.price)
print(fruta.power)
