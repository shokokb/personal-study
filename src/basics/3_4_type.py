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
    
    if type(param) is str:
        print(f"{param} is str")
    elif type(param) is int:
        print(f"{param} is int")
    elif type(param) is bool:
        print(f"{param} is bool")
    elif param is None:
        print(f"{param} is None")
    elif isinstance(param, Dog):
        print(f"{param.name} is a dog")
    else:
        print("???")



    if type(param) in (str, int):
        print(f"{param} is str or int")

if __name__ == "__main__":
    main()