def myfunc():
    yield 'one'
    yield 'two'
    yield 'three'

if __name__ == "__main__":
        my = myfunc()
    print(next(my))
    print(next(my))
    print(next(my))
    # for x in myfunc():
    #     print(x)
    # print(myfunc())

    g = (i for i in range(10))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
