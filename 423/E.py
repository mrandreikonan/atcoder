N, Q = map(int, input().split())
A = list(map(int, input().split()))
for _ in range(Q):
    L, R = map(int, input().split())
    L -= 1
    R -= 1
    DIFF = R - L + 1
    S = [0] * DIFF
    F = [0] * DIFF
    S[0] = A[R]
    for i in range(1,DIFF):
        S[i] = S[i-1] + A[R-i]

    F[0] = S[DIFF-1]
    for i in range(1,DIFF):
        F[i] = F[i-1]-S[i-1]+S[DIFF-i-1]
    
    print(sum(F))