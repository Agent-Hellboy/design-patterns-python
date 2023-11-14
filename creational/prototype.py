from abc import ABC, abstractmethod
from copy import deepcopy

class Shape(ABC):
    @abstractmethod
    def clone(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def clone(self):
        return deepcopy(self)

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def clone(self):
        return deepcopy(self)

class ShapeFactory:
    shapes = {}

    @staticmethod
    def register_shape(shape_name, shape_obj):
        ShapeFactory.shapes[shape_name] = shape_obj

    @staticmethod
    def create_shape(shape_name):
        if shape_name in ShapeFactory.shapes:
            return ShapeFactory.shapes[shape_name].clone()
        else:
            raise ValueError("Shape not found in factory")

# Usage
ShapeFactory.register_shape('circle', Circle(5))
ShapeFactory.register_shape('square', Square(10))

circle = ShapeFactory.create_shape('circle')
print(circle.area())  # Output: 78.5

square = ShapeFactory.create_shape('square')
print(square.area())  # Output: 100
