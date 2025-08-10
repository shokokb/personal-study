# coding : UTF-8
    
def main():
    param1 = 1
    param2 = 2
    param1, param2 = param2, param1
    print(param1, param2) # 2 1

    l = [0, 1, 2, 3, 4]
    l[2], l[4] = l[4], l[2]
    print(l) # [0, 1, 4, 3, 2]

if __name__ == "__main__":
    main()