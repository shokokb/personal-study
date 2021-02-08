# coding: UTF-8

if __name__ == "__main__":
    l = [1, 2, 3, 4, 5]

    # インデックス
    for i in range(len(l)):
        print("index=", i)

    # インデックス＆要素
    for i, n in enumerate(l):
        print("enumerate", i, n)

    # リストの連結
    a = [1, 2, 3]
    b = [4, 5, 6]
    print(a + b)
    # b += a
    b.extend(a)
    print(b)

    # 逆順アクセス
    for n in l[::-1]:
        print("reverse=", n)

    #昇順ソート
    list_unsort = [1, 5, 4, 2, 3]
    print("asc=", sorted(list_unsort))

    list_unsort = [1, 5, 4, 2, 3]
    list_unsort.sort()
    print("asc=", list_unsort)

    # 降順ソート
    list_unsort = [1, 5, 4, 2, 3]
    list_unsort.sort(reverse=True)
    print("desc=", list_unsort)

    # 逆順
    list_unsort = [1, 5, 4, 2, 3]
    print(list_unsort[::-1])
    list_unsort.reverse()
    print(list_unsort)

    # 逆順イテレータ
    list_unsort = [1, 5, 4, 2, 3]
    # print("desc=", list(reversed(list_unsort)))
    for n in reversed(list_unsort):
        print(n)

    # 検索
    l = [1, 5, 4, 2, 3]
    print("find index=", l.index(5))  #

    # スライス
    # 文字列には直接代入できないが、スライスはできる
    l[2:4] = [1, 2]
    print(l)
    l[2:4] = []
    print(l)

    # stack(List)
    # 挿入
    print("stack - list")
    l = []
    l.append(1)
    l.append(2)
    l.append(3)
    print(l)
    # pop
    print("LIFO=", l.pop())

    # queue(List)
    # 挿入
    print("queue - list")
    l = []
    l.append(1)
    l.append(2)
    l.append(3)
    print(l)
    # pop
    print("FIFO=", l.pop(0))

    #index
    r = [1, 2, 3, 4, 5, 1, 2, 3]
    print("index", r.index(3, 3))

    # count
    print("count", r.count(2))

    # exist
    print(5 in r)

    # remove
    l = [1, 2, 2, 3, 4]
    l.remove(2)
    print(l)

    # del
    l = [1, 2, 3, 4, 5]
    del l[2]
    print(l)

    # 参照渡し
    j = [1, 2, 3, 4, 5]
    i = j
    i[0] = 100
    print(j)

    j = [1, 2, 3, 4, 5]
    i = j.copy()
    i[0] = 100
    print(j)

    l = [[1, 4], [2, 3], [1, 5]]
    l = sorted(l, key=lambda x: (-x[0], -x[1]))
    print(l)
