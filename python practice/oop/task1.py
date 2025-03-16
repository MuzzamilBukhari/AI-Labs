class Car:
    __total_cars = 0
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.__total_cars += 1

    def fullName (self):
        return f"Car brand is {self.__brand} and Model is {self.__model}"

    @staticmethod
    def general_description():
        return 'Car is a mean of transport'

    def get_model(self):
        return self.__model

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    


my_car = Car('Toyota', 'Corolla')
electric_car = ElectricCar('Honda', 'Civic', '100KWh')
electric_car = ElectricCar('Honda', 'City', '120KWh')

# print(electric_car.fullName())
# print(electric_car.get_brand())
my_car.__model = 'city'
# print(my_car.general_description()) # it works 
# print(Car.general_description())   # it works

print(my_car.__model)