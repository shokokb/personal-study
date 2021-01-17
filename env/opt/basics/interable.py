# coding: utf-8
# Your code here!
list_all = [1,1,1,1,1,1,1]
print("all", all(n == 1 for n in list_all))

list_any = [1,3,5]
print("any", any(n == 2 for n in list_any))
print("any", any(n == 3 for n in list_any))

list_list = [1,2,3]
list_itr = iter(list_list)
print(next(list_itr))
print(next(list_itr))

def is_even (n):
    return n % 2 == 0
list_filter = list(filter(is_even, [1,2,3,4,5]))
print(list_filter)

list_filter2 = list(filter(lambda n: n % 2 == 0, [1,2,3,4,5]))
print(list_filter2)

list_map = list(map(lambda x: 2 * x, range(5)))
print(list_map)