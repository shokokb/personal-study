# coding: UTF-8

import time
from typing import List

class StringBuilder:
    def __init__(self):
        self.arr = []

    def joinWords(self, words:List[str]) -> (str, float):
        start = time.time()
        for word in words:
            self.arr.append(word)
        # ans = ""
        # for word in words:
        #     ans += word
        elapsed_time = time.time() - start
        return "".join(self.arr), elapsed_time

if __name__ == "__main__":
    words = []
    for _ in range(10000):
        words.append("Hello")

    sb = StringBuilder()
    print(sb.joinWords(words))
    # 0.001049041748046875