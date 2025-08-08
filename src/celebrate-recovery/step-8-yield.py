# coding : UTF-8

def tell_good_news():
    messages = [
        "God is with you💓",
        "You are the light of the world💡 - Matthew 5:14",
        "Your sins are forgiven✝️ - Luke 7:48",
        "I am with you always🌈 - Matthew 28:20",
    ]
    while True:
        for message in messages:
            yield message

def main() :
    alive = tell_good_news()
    try : 
        print(next(alive))
        print(next(alive))
        print(next(alive))
    except StopIteration:
        print("Now, you are in the Heaven👼")

if __name__ == "__main__":
    main()

# Matthew 5:10
