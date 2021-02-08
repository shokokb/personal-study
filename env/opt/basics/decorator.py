# coding: UTF-8


def price_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

@price_info
def add_num(a, b):
    return a + b 

if __name__ == "__main__":
    # f = price_info(add_num)
    # print(f(10, 20))
    print(add_num(10, 20))