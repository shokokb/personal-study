# coding : UTF-8

def main():
    fruits = {"Apple", "Grape", "Orange"}
    for fruit in fruits:
        print(fruit)
    
    print("Apple" in fruits)    # O(1)
    print("Banana" in fruits)

    fruits.add("Kiwi")
    print(fruits)
    fruits.remove("Grape")
    print(fruits)

if __name__ == "__main__":
    main()