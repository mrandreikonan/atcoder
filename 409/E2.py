import sys
input = sys.stdin.readline
sys.setrecursionlimit(1 << 25)


N = int(input())
X = list(map(int,input().split()))

G = [[] for _ in range(N)]

ans = 0

for edge in range(N-1):
    u, v, w = map(int, input().split())
    G[u-1].append((v-1, w))
    G[v-1].append((u-1, w))

def DFS(v, parent):
    global ans
    global X
    for u, w in G[v]:
        if u == parent:
            continue
        sub = DFS(u, v)
        ans += abs(sub) * w
        X[v] += sub

    return X[v]

DFS(0, -1)
print(ans)