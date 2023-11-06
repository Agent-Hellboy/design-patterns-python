from abc import ABC, abstractmethod
from typing import List

class IceCreamBuilder(ABC):
    @abstractmethod
    def add_topping(self) -> None:
        """Add a topping to the ice cream."""
        pass

class Icecream:
    def __init__(self, base_price: float):
        self.toppings: List = []
        self.price: float = base_price

    def add_topping(self, topping: 'Topping') -> 'Icecream':
        """
        Add a topping to the ice cream.

        Args:
            topping (Topping): The topping to be added.

        Returns:
            Icecream: The updated Icecream object.
        """
        self.toppings.append(topping)
        return self

    def cal_final_price(self) -> float:
        """
        Calculate the final price of the ice cream.

        Returns:
            float: The final price of the ice cream.
        """
        return self.price + sum([top.price for top in self.toppings])

class Basic:
    price: float = 3

class Vanilla:
    price: float = 5

class AIceCream:
    price: float = 10

icecream = Icecream(AIceCream()).add_topping(Basic()).add_topping(Vanilla())