from collections import deque

H, W = map(int, input().split())

S = []
U = []

ans = 0
queue = deque()

#dir = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def checkOnlyOneBlack(h, w):
    global dir
    global S
    global H
    global W
    global U

    ret = True
    blacks = 0

    for d in dir:
         x = h + d[0]
         y = w + d[1]

         if (x >= 0) and \
            (x < H)  and \
            (y >= 0) and \
            (y < W)  and \
            (S[x][y] == False):
            blacks += 1
            if blacks > 1:
                ret = False
                break
    
    if ret == False:    
        return ret
    else:
        return (blacks == 1)
           

for i in range(H):
    S.append([])
    U.append([])

    s = input()
    for index, ch in enumerate(s):
        U[i].append(False)

        if ch == "#":
            ans += 1
            S[i].append(False)
            U[i][index] = True
            queue.append((i, index))
        else:
            S[i].append(True)

while (len(queue) > 0):
    
    ln = len(queue)
    cand = []

    for i in range(ln):
        cell = queue.popleft()
        for d in dir:
            h = cell[0] + d[0]
            w = cell[1] + d[1]

            if (h >= 0) and (h < H)  and (w >= 0) and (w < W):
                if (U[h][w] == False) and (S[h][w] == True) and (checkOnlyOneBlack(h,w) == True):
                    cand.append((h,w))
                    U[h][w] = True

    for i in range(len(cand)):
        ans += 1
        h = cand[i][0]
        w = cand[i][1]
        S[h][w] = False
        queue.append((h,w))                    

print(ans)
