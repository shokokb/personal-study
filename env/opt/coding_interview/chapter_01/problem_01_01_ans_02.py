# coding: UTF-8
from typing import List
from collections import defaultdict

def is_unique_char (sentence:str) -> bool:
    # もし、ASCII文字だけであるのであれば、128文字を超過する場合は、重複する
    if len(sentence) > 128:
        return False
    l = [False for i in range(128)]
    for c in sentence:
        if l[ord(c) - ord('a')]:
            return False
        l[ord(c) - ord('a')] = True
    return True

if __name__ == "__main__":
    result = is_unique_char("abca")
    print(result)

