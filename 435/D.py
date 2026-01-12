from collections import deque

N, M = map(int, input().split())

C = [0 for i in range(N)]
G = [[] for i in range(N)]

ans = [False for i in range(N)]

for i in range(M):
    X, Y = map(int, input().split())
    G[Y-1].append(X-1)

def BFS(G, C, ans, v):
    Q = deque()
    Q.append(v)
    ans[v] = True

    while len(Q) > 0:
        u = Q.popleft()
        for ver in G[u]:
            if ans[ver] == False:
                ans[ver] = True
                Q.append(ver)


Q = int(input())
for _ in range(Q):
    q = input().split()
    action = int(q[0])
    v = int(q[1]) - 1

    if action == 1:
        if C[v] == 0:
            C[v] = 1
            if False == ans[v]:
                BFS(G, C, ans, v)
    else:
        if True == ans[v]:
            print('Yes')
        else:
            print('No')