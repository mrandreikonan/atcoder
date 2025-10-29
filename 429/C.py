N = int(input())
A = list(map(int, input().split()))
A = sorted(A)

ans = 0

M = 1
el = A[0]

for i in range(1, N):
    if A[i] == el:
        M += 1
        if i == N-1:
            ans += M * (M-1) * (N-M) // 2
    else:
        if M > 1:
            ans += M * (M-1) * (N-M) // 2

        el = A[i]
        M = 1

print(ans)