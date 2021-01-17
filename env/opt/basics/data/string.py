# coding: utf-8
# Your code here!
print("x" * 5)

str = "hello world"
print(str[:3])
print(str[3:])
print(str[0:len(str):2])

print("ord", ord("％"))
print("chr", chr(65285))

print(str.split())
print(str.partition(" "))

print(str.count("l")) # l が何個あるか
print("ascii", ascii(str))
print("encode", str.encode()) #'b"hello world" バイト型

print(str.find("l"))
print(str.find("x"))
print(str.rfind("l"))
print(str.index("l"))

x = b'abc'
y = bytearray(x)
print("bytearray", y[0])

ans = eval("1+2")
print(ans)

exec("a = 1 + 4")
exec("print(a)")