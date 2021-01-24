# coding: UTF-8
from typing import List
from collections import Counter

# Time Complexity = O(N)
def urlify (sentence:str) -> bool:
    sentence = sentence.lower()
    c = Counter(sentence)
    print(c)
    odd = list(filter(lambda v: v % 2 == 1, c.values()))
    return len(odd) == 1

if __name__ == "__main__":
    result = urlify("TactCoapapa")
    print(result)