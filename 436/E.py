N = int(input())
P = list(map(int, input().split()))

V = [False for _ in range(N)]
ans = 0

for i in range(N):
    if V[i] == True:
        continue
    
    L = 0
    x = i

    while V[x] == False:
        V[x] = True
        x = P[x] - 1
        L += 1

    if L > 1:
        ans += (L - 1) * L // 2

print(ans)