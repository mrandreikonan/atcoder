from collections import deque

H, W = map(int, input().split())
M = [[0 for i in range(W)] for j in range(H)]
V = [[False for i in range(W)] for j in range(H)]
J = [[] for i in range(27)]

def BFS(H, W, M, V, x, y):

    mv = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    Q = [deque(), deque()]
    Qidx = 0
    Q[Qidx].append((x,y))
    V[0][0] = True

    ans = 0
    found = False

    while len(Q[Qidx]) > 0:
        h, w = Q[Qidx].popleft()

        # 2 8
        # 4 2

        if (h == H-1) and (w == W-1):
            found = True
            break


        # 4 classic moves
        for dh, dw in mv:
            nh, nw = h + dh, w + dw
            if (nh >= 0) and (nh < H) and (nw >= 0) and (nw < W) and (M[nh][nw] >= 0) and (V[nh][nw] == False):
                Q[abs(1 - Qidx)].append((nh, nw))
                V[nh][nw] = True
        
        # jumps
        if M[h][w] > 0:
            for nh, nw in J[M[h][w]]:
                if V[nh][nw] == False:
                    Q[abs(1 - Qidx)].append((nh, nw))
                    V[nh][nw] = True
            J[M[h][w]] = []
        
        if len(Q[Qidx]) == 0:
            Qidx = abs(1 - Qidx)
            ans += 1
    
    if found == True:
        return ans
    else:
        return -1

for i in range(H):
    S = input()
    for j in range(W):
        if S[j] == '.':
            M[i][j] = 0
        elif S[j] == '#':
            M[i][j] = -1
        else:
            M[i][j] = ord(S[j]) - ord('a') + 1
            J[M[i][j]].append((i,j))


print(BFS(H, W, M, V, 0, 0))