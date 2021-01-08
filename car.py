# # class

# class Car():
#     def __init__(self, make, model, color):
#         self.make = make
#         self.model = model
#         self.color = color
#         self.gas = 100

#     def __str__(self):
#         return "{}, {}, {}".format(self.make, self.model, self.color)

#     def drive(self):
#         self.gas -= 10
#         print(self.gas)

#     def fill_tank(self):
#         self.gas = 100


# car1 = Car("Audi", "RS3", "Grey")


# car1.drive()
# car1.drive()


class Driver():
    def __init__(self, name, team, car,):
        self.name = name
        self.team = team
        self.car = car
        self.points = 0

    def __str__(self):
        return "{}, {}, {},".format(self.name, self.team, self.car)

    def win(self):
        self.points += 25
        print(self.points)

    def reset_season(self):
        self.points = 0
        print(self.points)

    def check_points(self):
        print(self.points)


driver1 = Driver("Fernando Alonso", "Renault", "RN240")

driver1.win()
driver1.win()
driver1.check_points()
driver1.reset_season()
