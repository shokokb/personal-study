# coding: utf-8
# Your code here!

t = (1,"apple",2,"orange",3)
print(type(t))
print(len(t))
for v in t:
    print(v)

# Tupleはインデックスを持つ
t = ((1, "gold"), (2, "silver"), (3, "bronze"))
for i, color in t:
    print(i, color)