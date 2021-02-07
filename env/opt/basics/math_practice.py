# coding: utf-8
import math

if __name__ == "__main__":
    print(int(2.5))
    print(float(1))
    print(round(3.5))
    d, e = divmod(5, 3)

    print("divmod", d, e)
    print("abs", abs(2 - 5))
    print("min", min(2, 3))
    print("max", max(5, 2))

    print("bool", bool(0))
    print("bool", bool("false"))
    print("bool", bool(""))

    print("bin", bin(5))
    print("oct", oct(8))
    print("hex", hex(15))

    print("complex", complex(2, 3))

    print("pow", 2**10)
    print("pow", pow(2, 10))

    pie = 3.1415
    print(pie)
    print(round(pie, 2))

    print(math.ceil(pie))
    print(math.floor(pie))
    print(math.sqrt(25))
    print(math.log2(8))

    print(help(math))