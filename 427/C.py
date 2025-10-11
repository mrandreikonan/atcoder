from collections import deque

N, M = map(int, input().split())
E = []
R = [False]*M
ans = M + 1

G = [[0 for j in range(N)] for i in range(N)]

for i in range(M):
    u, v = map(int, input().split())
    E.append((u-1,v-1))

for i in range(M):
    G[E[i][0]][E[i][1]] = 1
    G[E[i][1]][E[i][0]] = 1

def isBipartite(G, n):
    queue = deque()
    color = [-1]*n
    queue.append(0)
    color[0] = 0

    res = True

    while len(queue) > 0:
        node = queue.popleft()

        for j in range(N):
            if (node != j) and (G[node][j] == 1):
                neigh = j
            else:
                continue
            
            if color[neigh] == -1:
                color[neigh] = abs(color[node] - 1)
                queue.append(neigh)
            elif (color[neigh] == color[node]):
                res = False
                break

        if False == res:
            break

        if len(queue) == 0:
            for i in range(N):
                if color[i] == -1:
                    queue.append(i)
                    color[i] = 0
                    break

    return res

def solve(G, n, edges, level):
    global ans

    for e in edges:
        if G[e[0]][e[1]] == 1:

            G[e[0]][e[1]] = 0 
            G[e[1]][e[0]] = 0

            if True == isBipartite(G, n):
                if ans > level + 1:
                    ans = level + 1

                G[e[0]][e[1]] = 1
                G[e[1]][e[0]] = 1
                break
            else:
                solve(G, n, edges, level + 1)
                G[e[0]][e[1]] = 1
                G[e[1]][e[0]] = 1

if True == isBipartite(G, N):
    ans = 0
else:
    solve(G, N, E, 0)

print(ans)