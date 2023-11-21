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


**Date: 21 Nov 2023** 

#### An example from real-world codebase

https://github.com/dbader/schedule/blob/master/schedule/__init__.py#L208 


check how the library is using the builder pattern to build a Job object

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
The Singleton pattern is often used for:

- Logging
- Driver objects
- Caching
- Thread pools
- Database connections

In these scenarios, it's crucial to have only one instance for efficient resource utilization and coordination.

## Best Practices

The Singleton pattern is a powerful and versatile design pattern, but it should be used judiciously, as it can introduce global state and potential issues if misused. Proper implementation and consideration of threading and performance concerns are vital when applying the Singleton pattern.

## Conclusion

By understanding the Singleton pattern, you can design and implement classes that ensure global consistency and effective resource management in your software applications.

# Factory Design Pattern

**Date: 8 Nov 2023**

The Factory design pattern is a creational design pattern that provides an interface for creating objects but allows subclasses to alter the type of objects that will be created. It's used when you want to delegate the responsibility of instantiating objects to their respective subclasses, promoting flexibility and encapsulation in the object creation process.

## Key Characteristics

1. **Abstract Factory**: A Factory class defines an interface for creating objects, and concrete subclasses implement this interface to create specific types of objects.
   e.g., an abstract `CarFactory` with concrete factories like `SmallCarFactory` and `LargeCarFactory`.

2. **Client Delegates Object Creation**: The client code (consumer) delegates the object creation to the Factory, abstracting the process of object creation from the client code.

3. **Product Creation**: Factories produce objects (products) based on specific conditions or requirements, allowing you to vary the objects' type or configuration.

4. **Loose Coupling**: The Factory pattern promotes loose coupling between the client code and the created objects. Clients interact with objects through their common interfaces.

5. **Encapsulation**: Object creation logic is encapsulated within the factory classes, making it easier to manage and modify the creation process.

6. **Extensibility**: Adding new product types or variations is easier, as it involves creating new concrete factory classes, not modifying existing client code.

## Use Cases

The Factory pattern is commonly used in scenarios where object creation needs to be abstracted and customized:

- Creating different types of documents in a document editing application.
- Generating reports in a reporting system with various output formats.
- Creating different GUI elements in a graphical user interface library.

## Best Practices

To effectively implement the Factory pattern:

- Define a clear interface for factories, ensuring they return objects with a common base type.
- Encapsulate object creation within concrete factory classes, each responsible for producing specific object types.
- Use the Factory pattern to avoid tight coupling between client code and object creation logic.
- Promote reusability by extending the Factory pattern with new concrete factories for additional object types.

The Factory pattern is a valuable tool for creating objects in a flexible and extensible manner, providing a clean separation between client code and the details of object creation.


# Prototype Design Pattern

**Date: 14 Nov 2023**

The Prototype design pattern is a creational pattern that focuses on creating objects by cloning an existing instance, known as the prototype, rather than creating new objects using constructors. It enables the creation of new objects by copying an existing object, promoting flexibility and reducing the need for subclassing.

## Key Characteristics

1. **Prototype Object**: The pattern involves defining a prototype object, which serves as the template for creating new objects. These objects are cloned to produce new instances.

2. **Cloning Mechanism**: Object creation occurs by cloning the prototype object, which reduces the need for explicit constructors and subclassing. The `clone()` method is used to create new instances.

3. **Reduced Subclassing**: Instead of creating new objects through subclassing, the Prototype pattern utilizes cloning to produce new instances with desired initial states.

4. **Dynamic Object Creation**: It allows dynamic object creation at runtime, enabling the creation of complex objects more efficiently.

5. **Deep Copy vs. Shallow Copy**: Depending on the requirement, the prototype can be cloned as a shallow copy (copying references) or a deep copy (copying object contents), maintaining object integrity.

## Use Cases

The Prototype pattern is beneficial in scenarios where:

- Creating new objects by copying an existing object's state is more efficient than using constructors.
- Avoiding the creation of subclasses for different object configurations or states is preferred.
- Objects need to be dynamically created based on runtime conditions.

## Best Practices

To effectively implement the Prototype pattern:

- Ensure the prototype object implements a `clone()` method to create copies of itself.
- Use appropriate copying mechanisms (shallow or deep) based on the object's complexity and requirements.
- Implement a clear interface for prototype objects to provide a consistent way of cloning.
- Utilize the Prototype pattern to avoid unnecessary subclassing for object creation variations.

The Prototype pattern provides a flexible way to create objects by copying existing instances, offering advantages in scenarios where object creation involves complex configurations or dynamic runtime requirements.

This pattern simplifies object creation and promotes code reusability by eliminating the need for multiple constructors or subclassing variations.


## Structural Design Patterns

...

## Behavioral Design Patterns

...

## Contributing

Contributions are welcome! If you have any examples or improvements for the existing design patterns, feel free to submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
