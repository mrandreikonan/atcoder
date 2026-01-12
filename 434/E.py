N = int(input())

G = {}

for i in range(N):

    X, R = map(int, input().split())

    if (X-R) not in G:
        G[X-R] = [X+R]
    else:
        G[X-R].append(X+R)

    if (X+R) not in G:
        G[X+R] = [X-R]
    else:
        G[X+R].append(X-R)

visited = {v: False for v in G.keys()}

ans = 0

def isTree(G, v, visited):
    used = set()
    edgeCount = 0
    stack = [v]

    while stack:
        u = stack.pop()
        if u in used:
            continue
        else:
            used.add(u)
            visited[u] = True
            for uu in G[u]:
                edgeCount += 1
                stack.append(uu)

    edgeCount //= 2
    if len(used) == edgeCount + 1:
        return True, len(used)
    else:
        return False, len(used)


for v in G.keys():
    if visited[v] == True:
        continue
    else:
        tree, n = isTree(G, v, visited)
        if tree == True:
            ans += n-1
        else:
            ans += n

print(ans)