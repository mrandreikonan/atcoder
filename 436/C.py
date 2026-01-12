from sortedcontainers import SortedList

X = SortedList([])

N, M = map(int, input().split())
ans = 0

for _ in range(M):
    R, C = map(int, input().split())
    ptn = [R*N + C, R*N + C + 1, (R+1)*N + C, (R+1)*N + C+1]
    
    if (False == (ptn[0] in X)) and (False == (ptn[1] in X)) and (False == (ptn[2] in X)) and (False == (ptn[3] in X)):
        X.add(ptn[0])
        X.add(ptn[1])
        X.add(ptn[2])
        X.add(ptn[3])
        ans += 1

print(ans)