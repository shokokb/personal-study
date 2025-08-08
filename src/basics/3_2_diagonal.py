# coding : UTF-8:

import math

def pethagoras_theorem (w, h) :
    return math.sqrt(w ** 2 + h ** 2)

def main():
    width = 10
    height = 4
    diagnal = pethagoras_theorem(width, height)
    print(diagnal)

if __name__ == "__main__":
    main()