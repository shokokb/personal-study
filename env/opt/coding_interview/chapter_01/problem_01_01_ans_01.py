# coding: UTF-8
from typing import List
from collections import defaultdict

def is_unique_char (sentence:str) -> bool:
    # もし、ASCII文字だけであるのであれば、128文字を超過する場合は、重複する
    if len(sentence) > 128:
        return False
    h = defaultdict(lambda:False)
    for c in sentence:
        if h[c]:
            return False
        h[c] = True
    return True

if __name__ == "__main__":
    result = is_unique_char("abc")
    print(result)

