N, M = map(int, input().split())
A = list(map(int, input().split()))
s = sum(A)

ans = False

for i in range(N):
    if s - A[i] == M:
        ans = True
        break

if ans == True:
    print('Yes')
else:
    print('No')