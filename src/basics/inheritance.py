# coding : UTF-8

from abc import ABCMeta, abstractmethod

class Animal(metaclass = ABCMeta):
    name = ""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def cry(self):
        pass

class Dog(Animal):
    def cry(self):
        print("Woof")

def main():
    
    john = Dog("John")
    
    print(f"Hello, {john.name}")
    john.cry()

    if isinstance(john, Dog):
        print(f"{john.name} is a dog.")
    
    if isinstance(john, Animal):
        print(f"{john.name} is a animal.")

if __name__ == "__main__":
    main()