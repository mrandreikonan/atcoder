N = int(input())
A = list(map(int, input().split()))

ans = 1
last_fall = A[0]-1

for i in range(1,N):
    if (last_fall < i):
        break
    if (i <= last_fall):
        ans += 1
    if (i+A[i]-1 > last_fall):
        last_fall = i+A[i]-1

print(ans)