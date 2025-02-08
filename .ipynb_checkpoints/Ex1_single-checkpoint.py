"""
SINGLE INHERITANCE

Inheritance in Python's Object-Oriented Programming (OOP) allows one class to inherit the attributes and methods of another class. This helps in reusing code and creating a hierarchical relationship between classes.

Key Concepts of Inheritance
Base Class (Parent Class):
The class whose attributes and methods are inherited.

Derived Class (Child Class):
The class that inherits from the base class.
"""

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
   
    def speak(self):
        print(f"{self.name} barks")

dog = Dog("puppy")
dog.speak()  

"""

Inheritance: The Dog class inherits from the Animal class, which means it inherits the __init__ method and any other methods defined in Animal unless they are overridden.
Method Overriding: The speak method in the Dog class overrides the speak method in the Animal class. This allows the Dog class to provide its own specific implementation of the speak method.
Instance Creation and Method Call: When an instance of the Dog class is created and the speak method is called, the overridden method in the Dog class is executed, demonstrating polymorphism (the ability of different classes to be treated as instances of the same class through inheritance).
"""