# coding : UTF-8

from abc import ABCMeta, abstractmethod
from typing import Protocol

class IRunnable(Protocol):
    def run(self) -> bool:
        pass 

class ISwimmable(Protocol):
    def swim(self) -> bool:
        pass

class ICryable(Protocol):
    def cry(self) -> str:
        pass

class Animal(metaclass = ABCMeta):
    name = ""

    def __init__(self, name):
        self.name = name
    
class Dog(Animal, ICryable, IRunnable, ISwimmable):
    def __init__(self, name):
        super().__init__(f"{name}-kun")

    def cry(self) -> str:
        return "Woof"

    def run(self) -> bool:
        print("I'm running...")
        return True

    def swim(self) -> bool:
        print("I'm swimming...")
        return True

class Duck(Animal, ICryable, IRunnable, ISwimmable):
    def cry(self) -> str:
        return "Quack"

    def run(self) -> bool:
        print("I'm running...")
        return True

    def swim(self) -> bool:
        print("I'm swimming...")
        return True

class Fish(Animal, ICryable, IRunnable, ISwimmable):
    def __init__(self, name):
        super().__init__(f"{name}-kun")
    
    def cry(self) -> str:
        return "..."

    def run(self) -> bool:
        return False

    def swim(self) -> bool:
        print("I'm swimming...")
        return True

class Robot(IRunnable):
    def run(self) -> bool:
        return True
        
class Creator:
    def create(self, entity : ICryable):
        print(entity.cry())
    
    def make_entity_run(self, entity : IRunnable):
        if entity.run():
            print("Completed!")

def main():

    creator = Creator()    

    entities = [Dog("John"), Duck("Marry"), Fish("Nemo")]

    for entity in entities:

        print(f"Hello, {entity.name}")

        creator.create(entity)
        creator.make_entity_run(entity)

        # if isinstance(entity, Dog):
        #     print(f"{entity.name} is a dog.")

        # if isinstance(entity, Animal):
        #     print(f"{entity.name} is a entity.")

if __name__ == "__main__":
    main()