N, Q = map(int, input().split())
A = list(map(int, input().split()))
M = [0]*N

ans = 0

for q in range(Q):
    sq = A[q] - 1
    l = r = -1

    if (sq == 0): 
        l = 0
    else:
        l = M[sq - 1]

    if (sq == (N-1)):
        r = 0
    else:
        r = M[sq + 1]

    if M[sq] == 0:  
        if (l == 0 and r == 0):
            ans += 1
        elif (l == 1 and r == 1):
            ans -= 1
    else:
        if (l == 0 and r == 0):
            ans -= 1
        elif (l == 1 and r == 1):
            ans += 1

    M[sq] = abs(1 - M[sq])
    print(ans)
