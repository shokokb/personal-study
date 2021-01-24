# coding: UTF-8
from typing import List
from collections import Counter

# 大文字・小文字を同じとするか？
# 空白があるかどうか？
def exchange (sentence1:str, sentence2:str) -> bool:
    c1 = Counter(sentence1)
    c2 = Counter(sentence2)
    chrs = set(c1.keys()) | set(c2.keys())
    for c in chrs:
        if c1[c] != c2[c]:
            return False
    return True

if __name__ == "__main__":
    result = exchange("abc", "casb")
    print(result)
