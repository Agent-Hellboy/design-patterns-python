from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def drive(self):
        pass

class SmallCar(Car):
    def drive(self):
        return "Driving a small car"

class MediumCar(Car):
    def drive(self):
        return "Driving a medium car"

class LargeCar(Car):
    def drive(self):
        return "Driving a large car"

class CarFactory(ABC):
    @abstractmethod
    def create_car(self):
        pass

class SmallCarFactory(CarFactory):
    def create_car(self):
        return SmallCar()

class MediumCarFactory(CarFactory):
    def create_car(self):
        return MediumCar()

class LargeCarFactory(CarFactory):
    def create_car(self):
        return LargeCar()

# Client code
def drive_car(car_factory):
    car = car_factory.create_car()
    return car.drive()

small_car_factory = SmallCarFactory()
medium_car_factory = MediumCarFactory()
large_car_factory = LargeCarFactory()

print(drive_car(small_car_factory))
print(drive_car(medium_car_factory))
print(drive_car(large_car_factory))
