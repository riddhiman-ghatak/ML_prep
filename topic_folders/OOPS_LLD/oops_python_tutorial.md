# Object-Oriented Programming (OOP) in Python: A Complete Tutorial

## Introduction to OOP

Object-Oriented Programming (OOP) is a programming paradigm that organizes software design around data, or objects, rather than functions and logic. In Python, everything is an object, making it a very OOP-friendly language.

OOP makes your code more modular, reusable, and easier to maintain. It's especially useful for large programs where managing complexity is key.

### Key Concepts of OOP

1. **Class** - A blueprint for creating objects.
2. **Object** - An instance of a class.
3. **Encapsulation** - Hides the internal state of objects.
4. **Abstraction** - Hides complex logic and shows only necessary details.
5. **Inheritance** - Allows classes to inherit behavior from other classes.
6. **Polymorphism** - Methods behave differently based on the calling object.
7. **Composition & Aggregation** - Object relationships.
8. **Special Methods (Magic Methods)** - Enable operator overloading.
9. **Getters and Setters** - Provide controlled access to attributes.
10. **Decorators in OOP** - Such as `@abstractmethod`, `@property`, etc.

---

## 1. Classes and Objects

A **class** is a user-defined blueprint or prototype from which objects are created. An **object** is a collection of data (variables) and behaviors (methods).

```python
class Dog:
    def __init__(self, name):  # Constructor method
        self.name = name  # Instance attribute

    def bark(self):  # Method
        return f"{self.name} says woof!"

my_dog = Dog("Buddy")  # Create an object
print(my_dog.bark())  # Call a method
```

---

## 2. Encapsulation

Encapsulation means restricting direct access to some of an object’s components, which helps prevent accidental interference.

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance
```

Notice how `__balance` is private and cannot be accessed directly from outside the class.

---

## 3. Abstraction

Abstraction lets you focus on what an object does instead of how it does it. This is achieved using abstract base classes.

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof"
```

You can't create an instance of `Animal` directly—only its subclasses that implement `make_sound`.

---

## 4. Inheritance

Inheritance allows a class to use methods and properties of another class.

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def bark(self):
        return f"{self.name} says woof!"
```

Here, `Dog` inherits from `Animal`, gaining its attributes and methods.

---

## 5. Polymorphism

Polymorphism allows for using a unified interface for different types.

```python
class Cat:
    def speak(self):
        return "Meow"

class Dog:
    def speak(self):
        return "Woof"

def animal_sound(animal):
    print(animal.speak())
```

You can pass any object with a `speak()` method, and it will behave correctly.

---

## 6. Composition vs Aggregation

* **Composition**: Strong ownership. The contained object cannot exist without the container.
* **Aggregation**: The contained object can exist independently of the container.

```python
class Engine:
    def start(self):
        print("Engine starts")

class Car:
    def __init__(self):
        self.engine = Engine()  # Composition
```

---

## 7. Special (Magic) Methods

Magic methods enable operator overloading and are always surrounded by double underscores.

```python
class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return self.title  # For print()

    def __eq__(self, other):
        return self.title == other.title
```

---

## 8. Getters and Setters

Use `@property` and `@<name>.setter` to manage attribute access and validation.

```python
class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

item = Product(10)
item.price = 20  # Calls the setter
print(item.price)  # Calls the getter
```

---

## 9. Decorators in OOP

Decorators like `@abstractmethod`, `@property`, `@classmethod`, and `@staticmethod` add special functionality to methods.

### a. @abstractmethod

Defines a method that must be implemented by any subclass.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
```

### b. @property and @<name>.setter

Convert methods into managed attributes.

---

## 10. Advanced Features

### a. Class Methods and Static Methods

* `@classmethod`: Works with class-level data.
* `@staticmethod`: Utility method, doesn't access class or instance.

```python
class MyClass:
    count = 0

    @classmethod
    def increment_count(cls):
        cls.count += 1

    @staticmethod
    def greet():
        print("Hello from static method")
```

### b. Mixins

Mixins let you add optional behaviors to classes via multiple inheritance.

```python
class LogMixin:
    def log(self, message):
        print(f"[LOG]: {message}")

class MyService(LogMixin):
    def run(self):
        self.log("Service is running")
```

---

## Summary

This tutorial covered:

* Core OOP principles from beginner to advanced
* Python-specific syntax and idioms
* Getters and setters, abstract methods, decorators
* Practical examples and best practices

Mastering OOP is essential for scalable, maintainable Python software development.

Use these principles and techniques to write cleaner, more efficient, and reusable code in your projects!
