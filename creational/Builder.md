# Ice Cream Builder

This is a simple example of implementing the Builder pattern in Python to create custom ice creams with various toppings.

## Overview

The Ice Cream Builder pattern allows you to construct custom ice creams by adding different toppings. It provides a flexible and extensible way to create ice creams with varying combinations of toppings.

## Usage

To create an ice cream, follow these steps:

1. Create an instance of the `Icecream` class, providing the base price of the ice cream.
2. Use the `add_topping` method to add toppings to the ice cream. You can add as many toppings as you like.
3. Finally, call the `cal_final_price` method to calculate the final price of the ice cream.

Here's an example of creating an ice cream with the Builder pattern:

```python
from ice_cream import Icecream, Basic, Vanilla, AIceCream

# Create an ice cream with base price 10
icecream = Icecream(10)

# Add toppings
icecream.add_topping(Basic())
icecream.add_topping(Vanilla())

# Calculate final price
final_price = icecream.cal_final_price()

print(f"The final price of the ice cream is {final_price}.")
```

## Questions

  1 Why don't we have a Director class in this implementation?

    -> In this specific implementation, there is no separate "Director" class because the process of constructing the Icecream object is straightforward. 
       The Icecream class itself acts as the "Director" by allowing the client to add toppings to the ice cream using the add_topping method.

       By directly interacting with the Icecream class, the client has control over the construction process and can add toppings as desired. 
       This approach simplifies the code and eliminates the need for a separate Director class.
