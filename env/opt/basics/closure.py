# coding: UTF-8


def outer(a, b):
    def inner():
        return a + b
    return inner

def circle_area_func(pi):
    def circle_area(r):
        return r ** 2 * pi
    return circle_area


if __name__ == "__main__":
    f = outer(1, 2)
    print(f())
    c1 = circle_area_func(3)
    c2 = circle_area_func(3.14)
    print(c1(10))
    print(c2(10))