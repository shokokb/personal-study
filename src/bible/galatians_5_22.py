# coding : UTF-8

class Human:

    fruits = {"💗", "🤩", "🕊️", "🙏", "😊", "🎁", "🤝", "🧘", "⛓️"}

    def __init__(self):
        self._piece = input("What is your piece?")
    
    def is_fruit(self):
        return self._piece in Human.fruits

def main():
    me = Human()
    print(me.is_fruit())

if __name__ == "__main__":
    main()

