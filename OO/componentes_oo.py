# componentes - O.O

# Classe `class` - MateriaisdeEscritorio, Eletronico, Gadget, Fruta
# Objetos - Instancias ciradas a partir da classe - caneta, relógio, banana
# Atributos - Valores definidos nas classes e nos objetos (instancia)
# Método - Função definida no escopo da classe


class Person:  # pascalCase, UpperCamelCase
    """Represents a person."""
    company_name = "Dunder Mifflin"  #snake_case
    work_address = "Rua Stanton, Pensilvania"
    balance = 0

    # snake_case
    def add_points(person, value):  # Método
        if person.role == "Manager":
            value *= 2
        person.balance += value


jim = Person()
jim.name = "Jim Halpert"
jim.role = "Salesman"
jim.add_points(100)

# print(jim.name)
# print(id(jim))
# print(jim.company_name)
# print(jim.balance)

# print(Person.__dict__)
print(jim.__dict__)
