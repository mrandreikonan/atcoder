ans = 0
N = int(input())
for _ in range(N):
    A, B = map(int, input().split())
    if B > A:
        ans += 1
print(ans)