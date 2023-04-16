from Car import Car


class ElectricCars(Car):
    def __init__(self, year, make, model, batterySize):
        super().__init__(year, make, model)
        self.__battery = batterySize

    def showBattery(self):
        print(self.__battery)

    def description(self):
        info = f"{self.year}-{self.make}-{self.model}-{self.__battery}"
        return info.title()


e1 = ElectricCars(2019, "Tesla", "Model 3", 20)
print(e1.description())
e1.showBattery()


def printx(str2):
     if(str2)