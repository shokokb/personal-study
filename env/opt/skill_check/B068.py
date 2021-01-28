# coding: utf-8
ret = True
choco = ""
H, W = [int(m) for m in input().split()]
for i in range(H):
    a = [int(m) for m in input().split()]
    result = False
    for j in range(len(a)):
        if sum(a[0:j]) == sum(a[j:]):
            choco += ('A' * j) + ('B' * (len(a) - j)) + '\r\n'
            result = True
            break
    ret &= result
print("Yes" if ret else "No")
if ret:
    print(choco)

