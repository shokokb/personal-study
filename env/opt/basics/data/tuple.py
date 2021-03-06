# coding: utf-8

if __name__ == "__main__":
    t = (1,"apple",2,"orange",3)
    print(type(t))
    print(len(t))
    for v in t:
        print(v)

    # Tupleはインデックスを持つ
    t = ((1, "gold"), (2, "silver"), (3, "bronze"))
    for i, color in t:
        print(i, color)

    # index, count しかない
    # index
    t = (1,"apple",2,"orange",3, "apple")
    print(t.index(1))
    # count
    print(t.count("apple"))

    t = tuple(i for i in range(10))
    print(t)