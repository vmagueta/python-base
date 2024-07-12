
class Person:
    """Represents a person."""
    company_name = "Dunder Mifflin"
    work_address = "Rua Stanton, Pensilvania"
    balance = 0  # Atributo de classe IMUTÁVEL

    # Data Model - Método Dunder ou Métodos Mágicos
    def __init__(self, name, role="Undefined", prefered_colors=None):
        self.name = name
        self.role = role
        self.prefered_colors = prefered_colors or []

    # nunca defita um valor mutável como atributo de classe
    # prefered_colors = [] Atributo de classe mutável da classe

    # Injeção de dependência - 1° arg método = a própria instancia
    def add_points(self, value):
        if self.role == "Manager":
            value *= 2
        self.balance += value


# Consent Adults - Somos Adultos e sabemos o que fazemos

jim = Person(name="Jim Halpert", role="Salesman", prefered_colors=["Blue"])  # __init__ (inicializador da classe)
jim.add_points(500)
# jim.prefered_colors.append("Blue")  # altera para todas as instâncias
jim.work_address = "Home"
print(jim.name, jim.balance, jim.prefered_colors, jim.work_address, jim.role)

pam = Person("Pam Beasly", "Receptionist", ["Purple", "Yellow"])
# pam.prefered_colors.append("Purple")
pam.add_points(100)
print(pam.name, pam.balance, pam.prefered_colors, pam.work_address, pam.role)
