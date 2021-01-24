# coding: UTF-8
from typing import List

# Time Complexity = O(NlogN)
def urlify (sentence:str, length:int) -> str:
    return sentence.replace(" ", "%20")

if __name__ == "__main__":
    result = urlify("Mr John Smith", 13)
    print(result)