
class Vechile:
    def __init__(self,type_of_ship, number, fuel_amount, condition):
        self.type_of_ship = type_of_ship
        self.number = number
        self.fuel_amount = fuel_amount
        self.condition = condition

class Ticket:
    def __init__(self, owner_inicial):
        self.owner_inicial = owner_inicial



class Passanger:
    def __init__(self, inicials, ticket):
        self.inicials = inicials


class Staff:
    def __init__(self, staff_inicials, passport, post):
        self.staff_inicials = staff_inicials
        self.pasport = passport



