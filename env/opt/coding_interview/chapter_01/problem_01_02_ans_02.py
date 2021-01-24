# coding: UTF-8
from typing import List
from collections import Counter

# 大文字・小文字を同じとするか？
# 空白があるかどうか？
# Time Complexity = O(NlogN)
def exchange (sentence1:str, sentence2:str) -> bool:
    # O(NlongN)
    sentence1 = sorted(sentence1)
    sentence2 = sorted(sentence2)
    # print(sentence1, sentence2)
    # O(N)
    return sentence1 == sentence2

if __name__ == "__main__":
    result = exchange("abc", "cdb")
    print(result)
