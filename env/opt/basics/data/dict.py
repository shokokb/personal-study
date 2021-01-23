# coding: utf-8

from collections import defaultdict

print("=== dict ===")

hash1 = {}
hash1["apple"] = 120
hash1["banana"] = 100
print(hash1["banana"])
try:
    print(hash1["grape"])
except KeyError:
    print("key error exception")
except:
    print("other exception")
finally:
    print("finally")
    
hash2 = {"apple" : 120, "banana": 100}
print("hash2", hash2["apple"])

hash3 = dict(apple=120, banana=100)
hash4 = dict(grape=200, pear=300)
print("hash3", hash3)
print("hash4", hash4)
hash5 = dict(**hash3,**hash4)
print("hash5(連結)", hash5)

print("=== defaultdict ===")
hash6 = defaultdict(lambda: None)
print(hash6["grape"])
