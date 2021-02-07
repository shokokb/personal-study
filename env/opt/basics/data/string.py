# coding: utf-8
if __name__ == "__main__":

    print("I don't know")
    print('I don\'t know')
    # 改行
    print(r'C:\names\name')

    # srartWith
    s = "My name is Shoko"
    print(s.startswith('My'))
    if s.startswith('My'):
        print("Started with My")

    # 繰り返し
    print("x" * 5)

    # 文字列連結
    print("Py" + "thon")
    print("".join(["Py", "thon"]))
    print("Hi" * 3 + ", Mike!")
    print(f'{"Hi!" * 3}, Mike!')
    print('a is {}'.format('a'))
    print('a is {0} {1} {2}'.format(1, 2, 3))
    s = ('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' 'BBBBBBBBBBBBBBBBBBBBBBBBBBBBB')
    print(s)

    # スライス
    str = "hello world"
    print(str[:3])
    print(str[3:])
    print(str[0:len(str):2])
    word = "Python"
    word = "J" + word[1:]
    print(word)

    # ヒアドキュメント
    print("######")
    print("""\
line1
line2
line3\
    """)
    print("######")

    # 文字列長
    print(len("abc"))
 
    # find rfind
    s = 'My name is Mike Mikel'
    print("index", s.index('Mike'))
    print("find", s.find('Mike'))
    print("rfind", s.find('Mike'))

    # count
    print("count", s.count('Mike'))

    # capitalize
    s = 'my name is mike'
    print(s.capitalize())
    # title 
    print(s.title())
    # upper/lower
    print(s.upper())
    print(s.lower())
    
    # replace
    s = 'My name is Mike'
    s = s.replace('Mike', 'Nancy')
    print(s)

    print("ord", ord("％"))
    print("chr", chr(65285))

    print(str.split())
    print(str.partition(" "))

    print(str.count("l")) # l が何個あるか
    print("ascii", ascii(str))
    print("encode", str.encode()) #'b"hello world" バイト型

        


    x = b'abc'
    y = bytearray(x)
    print("bytearray", y[0])

    # === eval
    ans = eval("1+2")
    print(ans)

    exec("a = 1 + 4")
    exec("print(a)")
    
