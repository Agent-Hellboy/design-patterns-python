# Design Patterns

This repository contains examples of different design patterns implemented in Python. Design patterns are proven solutions to recurring problems in software design, and they provide a way to solve common design problems effectively.

## Creational Design Patterns

Creational design patterns focus on object creation mechanisms, trying to create objects in a manner suitable for the situation at hand. The following creational design patterns are covered:

### Builder Pattern

#### Date: 6 Nov 2023 

The Builder pattern separates the construction of an object from its representation, allowing the same construction process to create various representations. It provides a flexible and readable way to create complex objects step by step.

In the Builder pattern, a builder class is responsible for constructing the object. It provides methods to set the desired attributes or properties of the object. The client code uses the builder to construct the object and obtain the final result.

#### Why Ice Cream?

To explain the Builder pattern, the example of creating custom ice creams with various toppings is used. This example demonstrates how the Builder pattern allows the creation of complex objects (ice creams) step by step, by adding different toppings. The flexibility of choosing toppings and the ability to create custom ice cream combinations highlight the benefits of the Builder pattern.


# Singleton Design Pattern

**Date: 7 Nov 2023**

The Singleton design pattern is a creational design pattern that ensures a class has only one instance and provides a global point of access to that instance. It is used when exactly one object is needed to coordinate actions across the system. This single instance is shared and used throughout the application, providing a common point of interaction for different components.

## Key Characteristics

1. **Single Instance**: The Singleton pattern ensures that a class has only one instance, which is created lazily upon first access and shared across the application.

2. **Global Access**: The single instance is globally accessible, allowing other objects to access it without creating their own instances.
    e.g singalton DB connection 

3. **Lazy Initialization**: The instance is created when it is first requested, not at the time the class is loaded.

4. **Thread Safety**: Implementations must be thread-safe to prevent multiple threads from creating duplicate instances.

5. **Private Constructor**: The Singleton class typically has a private constructor to prevent direct instantiation.

6. **Global Point of Control**: It provides a centralized point of control for managing a shared resource or coordinating actions.

## Use Cases

The Singleton pattern is


## Structural Design Patterns

...

## Behavioral Design Patterns

...

## Contributing

Contributions are welcome! If you have any examples or improvements for the existing design patterns, feel free to submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.