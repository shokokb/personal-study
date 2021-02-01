# coding: UTF-8

def permutation(s:str, prefix:str):
    if len(s) == 0:
        print(prefix)
    else:
        for i in range(len(s)):
            rem = s[:i] + s[i+1:]
            permutation(rem, prefix + s[i])
    return ""

def get_permutation(s:str):
    permutation(s, "")

if __name__ == "__main__":
    get_permutation("abc")