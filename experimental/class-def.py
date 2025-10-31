# %%
class Car:

    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.tank = 0
        self.tank_cap = 60

    def fill_up(self):
        self.tank = self.tank_cap
# %%
my_car = Car("BMW", "W042")
print(my_car)
# %%
