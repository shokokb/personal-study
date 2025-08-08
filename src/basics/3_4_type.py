# coding : UTF-8

class Dog:
    name = ""

    def __init__(self, name):
        self.name = name

    def cry(self):
        print("Woof")

def main():
    hello = "Hello World!"
    num = 123
    judge = True

    # param = hello
    # param = num
    # param = judge
    # param = None

    param = Dog("John")
    param.cry()

    print(type(param))
    
    if isinstance(param, str): 
    # if type(param) is str:
        print(f"{param} is str")
    elif isinstance(param, int):
    # elif type(param) is int:
        print(f"{param} is int")
    elif isinstance(param, bool):
    # elif type(param) is bool:
        print(f"{param} is bool")
    elif param is None:
        print(f"{param} is None")
    elif isinstance(param, Dog):
    # elif param is Dog: # an instance is not a class 
        print(f"{param.name} is a dog")
    else:
        print("???")

    if isinstance(param, (str, int)):
    # if type(param) in (str, int):
        print(f"{param} is str or int")

    list1 = [1, 2, 3]
    list2 = list1
    list3 = [1, 2, 3]
    print(list1 is list2) # True because they are the same pointer.
    print(list1 is list3) # False because they are the diffferent pointer.

if __name__ == "__main__":
    main()