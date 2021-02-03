def myfunc():
    yield 'one'
    yield 'two'
    yield 'three'
for x in myfunc():
    print(x)
# print(myfunc())