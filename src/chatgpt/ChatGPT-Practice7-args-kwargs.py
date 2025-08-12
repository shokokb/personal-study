# coding : UTF-8

def func(*args, **kwargs): # parameters are immutable
    print(args) # (1, 2, 3)
    print(kwargs) # {'a': 4, 'b': 5}

def main():
    func(1, 2, 3, a=4, b=5)
    
if __name__ == "__main__":
    main()