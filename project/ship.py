
import random
class World:
    price = 100
    def buy_ticket(self):
        if not isinstance(self, Stuff) and self.ticket == 0 and self.money_amount > World.price:
            self.money_amount -= World.price
            self.ticket = random.randrange(1000, 10000)
            Cashier.passangers_list[self.pas_inicials] = self.ticket
        else:
            pass

    def change_price(self,new_price):
        if isinstance(self, Cashier):
            World.price = new_price
        else:
            print('you are not eligible to do this')


class Stuff(World):
    def __init__(self,stuff_inicials,age):
        self.stuff_inicials = stuff_inicials
        self.age = age

class Cashier(Stuff):
    passangers_list = {}
    def __init__(self,stuff_inicials,age,salary):
        self.pas_inicials = stuff_inicials
        self.age = age
        self.salary = salary

class Passanger(World):
    def __init__(self, pas_inicials,money_amount,  ticket = 0):
        self.pas_inicials = pas_inicials
        self.money_amount = money_amount
        self.ticket = ticket



Marta = Cashier('Marta_Beggins', 30,100)
Roman = Passanger('Roman_Zeppeli',100000)
Marta.buy_ticket()
Roman.buy_ticket()
Kolya = Passanger('Kolya Morozov',200000)
Kolya.buy_ticket()
print(Marta.passangers_list)
Kolya.change_price(2)
print(Kolya.price)
Marta.change_price(200)
print(Kolya.price)










'''class Ecscursion:
=======
class Ecscursion:
>>>>>>> e409db6b6d50873d9f3de64dbbf0d7199175c564
    passangers = {}
    def __init__(self, route, ship, recording, shedule):
        self.route = route
        self._ship = ship
        self._recording = recording
        self._shedule = shedule

    def get_passangers_list(self):
        return(passangers, len(passangers))

    def add_passangers(self,inicials,code):
        passangers[code] = inicials


class Vechile:
    def __init__(self,type_of_ship, number, fuel_amount, condition):
        self.type_of_ship = type_of_ship
        self.number = number
        self.fuel_amount = fuel_amount
        self.condition = condition


'''






