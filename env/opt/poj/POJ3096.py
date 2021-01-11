N = 6
R = 10
X = [1,7,15,20,30,50]

def solve():
    cnt = 0
    global N
    global R
    global X

    i = 0
    while i < N:
        s = X[i]
        i += 1
        while i < N and X[i] <= s + R: 
            i += 1
        p = X[i-1]
        cnt += 1
        while i <N and X[i] <= p + R: 
            i += 1
    print(cnt)
    
solve()
