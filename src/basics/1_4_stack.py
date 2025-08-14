def main():
    stack = []
    print(stack)

    stack.append("Blue") # push O(1)
    print("After pushing:", stack)

    stack.append("Green")
    print("After pushing:", stack)

    stack.append("Red")
    print("After pushing:", stack)

    try:
        item = stack.pop()
        print("After popping:", item, stack)

        item = stack.pop()
        print("After popping:", item, stack)

        item = stack.pop()
        print("After popping:", item, stack)

        item = stack.pop()
        print("After popping:", item, stack)
    except IndexError:
        print("Index Error")

if __name__ == "__main__":
    main()