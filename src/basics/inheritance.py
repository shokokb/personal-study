# coding : UTF-8

from abc import ABCMeta, abstractmethod
from typing import Protocol

class ICryable(Protocol):
    @abstractmethod
    def cry(self) -> str:
        pass

class Animal(metaclass = ABCMeta):
    name = ""

    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def cry(self) -> str:
        return "Woof"

class Duck(Animal):
    def cry(self) -> str:
        return "Quack"

def make_animal_cry (animal: ICryable):
    print(animal.cry())

def main():
    
    john = Dog("John")
    
    print(f"Hello, {john.name}")
    make_animal_cry(john)

    marry = Duck("Marry")
    print(f"Hello, {marry.name}")
    make_animal_cry(marry)

    if isinstance(john, Dog):
        print(f"{john.name} is a dog.")
    
    if isinstance(john, Animal):
        print(f"{john.name} is a animal.")

if __name__ == "__main__":
    main()