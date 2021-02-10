import random
lst = [1, 2, 4, 8, 10]
key = random.randint(1, 10)
print(str(key) + "が含まれるかチェックする")
print(lst)


def linear_search(k) -> int:
    for i, n in enumerate(lst):
        if n == k:
            return i
    return None


print("線形探索", linear_search(key))

lst.sort()


def binary_search(s, k, l) -> int:
    # print(l)
    if len(l) == 0:
        return None
    p = len(l) // 2
    if k == l[p]:
        return s + p
    if k < l[p]:
        return binary_search(0, k, l[:p])
    return binary_search(p + 1, k, l[p + 1:])


print("二分探索", binary_search(0, key, lst))