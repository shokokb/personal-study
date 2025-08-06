# coding : UTF-8

def life () :
    counter = 0

    def increase () :
        nonlocal counter
        counter = 1 if counter == 0 else 2 * counter
        return "💓" * counter

    return increase
    
def main():
    my_life = life()
    print(my_life()) # 💓 
    print(my_life()) # 💓💓
    print(my_life()) # 💓💓💓💓
    print(my_life()) # 💓💓💓💓💓💓💓💓

if __name__ == "__main__":
    main()

# Philippians 1:9

