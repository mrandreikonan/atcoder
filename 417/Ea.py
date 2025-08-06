# Задача: ABC417 E - A Path in A Dictionary
# Мэта: знайсці лексікографічна найменшы просты шлях ад X да Y
# Спосаб: на кожным кроку выбіраем найменшага суседа, з якога
# яшчэ можна трапіць у Y, абыходзячы ўжо выкарыстаныя вяршыні
# Для праверкі дасягальнасці выкарыстоўваем DFS з Y
# Згенеравана ChatGPT на падставе аўтарскага рашэння з афіцыйнага разбору

import sys
sys.setrecursionlimit(1 << 20)

t = int(input())
for _ in range(t):
    n, m, x, y = map(int, input().split())

    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, n + 1):
        graph[i].sort()

    used = [False] * (n + 1)
    path = []

    def dfs_reachable(v, reachable):
        reachable[v] = True
        for u in graph[v]:
            if not used[u] and not reachable[u]:
                dfs_reachable(u, reachable)

    cur = x
    used[cur] = True
    path.append(cur)

    while cur != y:
        reachable = [False] * (n + 1)
        dfs_reachable(y, reachable)

        found = False
        for nei in graph[cur]:
            if not used[nei] and reachable[nei]:
                cur = nei
                used[cur] = True
                path.append(cur)
                found = True
                break

        if not found:
            path = [-1]
            break

    print(*path)