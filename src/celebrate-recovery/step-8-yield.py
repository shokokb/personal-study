# coding : UTF-8

def pray():
    while True:
        yield "God is with you🌏"

def main() :
    survive = pray()
    try : 
        print(next(survive))
        print(next(survive))
        print(next(survive))
    except StopIteration:
        print("Now, you are in the Heaven👼")

if __name__ == "__main__":
    main()