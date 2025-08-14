# coding : UTF-8

# stack for parentheses
def check_parentheses (text):
    stack = []
    pairs = { 
        ")" : "(",
        "}" : "{",
        "]" : "["
     }
    for s in text: # O(n)
        if s in ["(", "{", "["]:
            stack.append(s)
        elif s not in pairs:
            return False
        else:
            if len(stack) <= 0:
                return False
            if stack[-1] == pairs[s]:
                stack.pop()
            else:
                return False            
        # print(stack)
    return not stack

def main():
    print(check_parentheses("{[()]}"))  # True
    print(check_parentheses("{[(])}"))  # False
    print(check_parentheses("(){}[]"))  # True

if __name__ == "__main__":
    main()