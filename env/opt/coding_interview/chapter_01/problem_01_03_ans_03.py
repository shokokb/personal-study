# coding: UTF-8
from typing import List

# Time Complexity = O(NlogN)
def urlify (sentence:str, length:int) -> str:
    cnt = sentence.count(" ")
    ret = ["" for i in range(length + 2 * cnt)]
    sentence_list = list(sentence)
    i = len(ret) - 1
    while sentence_list:
        c = sentence_list.pop()
        if c == " ":
            ret[i-0] = "0"
            ret[i-1] = "2"
            ret[i-2] = "%"
            i -= 3
        else:
            ret[i] = c
            i -= 1
    return "".join(ret)

if __name__ == "__main__":
    result = urlify("Mr John Smith", 13)
    print(result)