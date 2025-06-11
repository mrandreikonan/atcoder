import sys
import heapq
from atcoder.dsu import DSU

input = sys.stdin.readline

N, Q = map(int, input().split())
V = []

for _ in range(N):
    x, y = map(int, input().split())
    V.append((x,y))

def d(i, j):
    vx, vy = V[i]
    ux, uy = V[j]
    return abs(vx - ux) + abs(vy - uy)

def unite(d, i, j):
    return (d << 32) | (i << 16) | j

MASK = 2**16 - 1
def split(element):
    return element >> 32, (element >> 16) & MASK, element & MASK

pQ = []
for i in range(N):
    for j in range(i+1, N):
        pQ.append(unite(d(i,j), i, j))

heapq.heapify(pQ)

dsu = DSU(N + Q)

for _ in range(Q):
    query = input()
    param = list(map(int,query.split()))

    if param[0] == 1:
        V.append((param[1], param[2]))
        n = len(V)
        for i in range(n-1):
            heapq.heappush(pQ, unite(d(i, n-1), i, n-1))            

    elif param[0] == 2:
        ans = -1
        while (len(pQ) > 0):
            dist, v, u = split(heapq.heappop(pQ))
            if False == dsu.same(v, u):
                dsu.merge(v,u)
                ans = dist
                while(len(pQ) > 0):
                    di, vi, ui = split(pQ[0])
                    if di != dist:
                        break
                    heapq.heappop(pQ)
                    if False == dsu.same(vi, ui):
                        dsu.merge(vi, ui)
                break
        
        print(ans)
        
    else:
        if True == dsu.same(param[1] - 1, param[2] - 1):
            print('Yes')
        else:
            print('No')