N = int(input())
L = list(map(int,input().split()))

l = 0
for i in range(N):
    if L[i] == 0:
        l += 1
    else:
        break

r = N
for i in range(N-1, 0, -1):
    if L[i] == 0:
        r -= 1
    else:
        break

if (l >= r):
    print(0)
else:
    print(r - l -1)