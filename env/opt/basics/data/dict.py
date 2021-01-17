# coding: utf-8
# Your code here!
hash = {}
hash["apple"] = 120
hash["banana"] = 100
print(hash["banana"])
try:
    print(hash["grape"])
except KeyError:
    print("key error exception")
except:
    print("other exception")
finally:
    print("finally")
    
hash1 = {"apple" : 120, "banana": 100}
print("hash1", hash1["apple"])

hash2 = dict(apple=120, banana=100)
print("hash2", hash2["apple"])

hash3 = dict(grape=200, pear=300)
hash4 = dict(**hash2,**hash3)
print(hash4)
