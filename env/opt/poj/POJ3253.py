N = 15
L = [3,4,5,1,2]

def solve():
    global N
    global L

    cost = 0
    while(len(L) > 1):
        L.sort()
        # print("start", L)
        L0 = L.pop(0)
        L1 = L.pop(0)
        Lmin = L0 + L1
        cost += Lmin
        L.insert(0, Lmin)
        # print("end", L, cost)







solve()
