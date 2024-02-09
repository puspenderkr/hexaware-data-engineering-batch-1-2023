# Creating a simple class
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")

# Creating an object of the class
my_dog = Dog("Buddy", 3)

# Accessing object attributes and calling a method
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.bark()


# Using access specifiers in Python
class MyClass:
    def __init__(self):
        self.public_var = "Public Variable"
        self._protected_var = "Protected Variable"
        self.__private_var = "Private Variable"

obj = MyClass()

# Accessing variables
print(obj.public_var)
print(obj._protected_var)
# The following line will result in an AttributeError as it is a private variable
# print(obj.__private_var)


# Using a constructor in a class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Alice", 25)
print(f"{person1.name} is {person1.age} years old.")


# Implementing inheritance in Python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog()
cat = Cat()

print(dog.speak())
print(cat.speak())