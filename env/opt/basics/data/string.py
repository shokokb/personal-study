# coding: utf-8
if __name__ == "__main__":

    print("I don't know")
    print('I don\'t know')
    # 改行
    print(r'C:\names\name')

    # 繰り返し
    print("x" * 5)

    # 文字列連結
    print("Py" + "thon")
    print("".join(["Py", "thon"]))
    print("Hi" * 3 + ", Mike!")
    s = ('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' 'BBBBBBBBBBBBBBBBBBBBBBBBBBBBB')
    print(s)

    # スライス
    str = "hello world"
    print(str[:3])
    print(str[3:])
    print(str[0:len(str):2])

    # ヒアドキュメント
    print("######")
    print("""\
line1
line2
line3\
    """)
    print("######")
 
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

    # === EVAL
    ans = eval("1+2")
    print(ans)

    exec("a = 1 + 4")
    exec("print(a)")
