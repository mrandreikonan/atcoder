T = int(input())

def calculatePower(G, H, W):
    res = []
    for i in range(H):
        res.append([0]*W)

    blackSquares = 0

    for i in range(H-1):
        for j in range(W-1):
            if (G[i][j] == 1) and (G[i+1][j] == 1) and (G[i][j+1] == 1) and (G[i+1][j+1] == 1):
                res[i][j] +=1
                res[i+1][j] +=1
                res[i][j+1] +=1
                res[i+1][j+1] += 1
                blackSquares += 1

    return res, blackSquares

for _ in range(T):
    H, W = map(int, input().split())

    G = []
    P = []
    ans = 0

    for i in range(H):
        S = input()
        G.append([0]*W)
        P.append([0]*W)
        for j in range(W):
            if (S[j] == '.'):
                G[i][j] = 0
            else:
                G[i][j] = 1

    P, bS = calculatePower(G, H, W)

    if bS == 0:
        print('0')
    else:
        while bS > 0:
            mx = X = Y = -1
            for i in range(H):
                for j in range(W):
                   if P[i][j] > mx:
                       mx = P[i][j]
                       X = i
                       Y = j
            
            G[X][Y] = 0
            ans += 1
            P, bS = calculatePower(G, H, W)
        print(ans)