N, Q = map(int, input().split())
A = list(map(int, input().split()))
for i in range(N):
    A.append(A[i])
S = [0] * (2*N)
for i in range(2*N):
    if i > 0:
        S[i] = S[i-1] + A[i]
    else:
        S[i] = A[i]

window_start = 0

for q in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 2:
        ans = 0
        l = query[1] - 1 + window_start
        r = query[2] - 1 + window_start
        if l == 0:
            ans = S[r]
        else:
            ans = S[r] - S[l-1]
        print(ans)
    else:
        c = query[1]
        window_start += c
        window_start %= N