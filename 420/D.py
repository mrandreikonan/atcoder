
import sys

sys.setrecursionlimit(100000000)

H, W = map(int, input().split())
A = []
V = [[0 for _ in range(W)] for _ in range(H)]
for i in range(H):
    A.append(input())

ans = sys.maxsize
move = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def validMoveCell(loc):
    if (loc[0] >= 0) and (loc[0] < H) and (loc[1] >= 0) and (loc[1] < W) and (A[loc[0]][loc[1]] != '#') and (V[loc[0]][loc[1]] < 2):
        return True

def DFS(start, switch_count, len):
    global ans

    if A[start[0]][start[1]] == 'G':
        if len < ans:
            ans = len
        return
    
    for mv in move:
        target = (start[0] + mv[0], start[1] + mv[1])
        if validMoveCell(target):
            if (A[target[0]][target[1]] == 'o' and switch_count % 2 == 0) or \
               (A[target[0]][target[1]] == 'x' and switch_count % 2 == 1) or \
               (A[target[0]][target[1]] == '.') or \
               (A[target[0]][target[1]] == 'G') or \
               (A[target[0]][target[1]] == 'S'):
                V[target[0]][target[1]] += 1
                DFS(target, switch_count, len + 1)
                V[target[0]][target[1]] -= 1
            elif A[target[0]][target[1]] == '?':
                V[target[0]][target[1]] += 1
                DFS(target, switch_count + 1, len + 1)
                V[target[0]][target[1]] -= 1
    

start = (-1, -1)
for i in range(H):
    for j in range(W):
        if A[i][j] == 'S':
            start = (i, j)
            break

    if start[0] != -1:
        break

DFS(start, 0, 0)
print(ans)