# coding : UTF-8

def decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper

@decorator
def greet():
    print("Hello!")

def main() :
    greet()
    # Because greet function has @decorator,
    # it prints
    #   Before the function call
    #   Hello!
    #   After the function call

if __name__ == "__main__":
    main()