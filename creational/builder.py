from abc import ABC, abstractmethod
from typing import List

class Topping(ABC):
    price: float

class Basic(Topping):
    price = 3

class Vanilla(Topping):
    price = 5

class IceCreamBuilder(ABC):
    @abstractmethod
    def add_topping(self, topping: Topping) -> None:
        """Add a topping to the ice cream."""
        pass

class Icecream(IceCreamBuilder):
    def __init__(self, base_price: float):
        self.toppings: List[Topping] = []
        self.price: float = base_price

    def add_topping(self, topping: Topping) -> 'Icecream':
        """
        Add a topping to the ice cream.

        Args:
            topping (Topping): The topping to be added.

        Returns:
            Icecream: The updated Icecream object.
        """
        self.toppings.append(topping)
        return self

    def calc_final_price(self) -> float:
        """
        Calculate the final price of the ice cream.

        Returns:
            float: The final price of the ice cream.
        """
        return self.price + sum([top.price for top in self.toppings])

# Example usage:
base_price = 10  # You can set your desired base price here.
ice_cream = Icecream(base_price).add_topping(Basic()).add_topping(Vanilla())
final_price = ice_cream.calc_final_price()
print(f"The final price of the ice cream is ${final_price:.2f}")
