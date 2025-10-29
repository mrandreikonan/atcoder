T = int(input())

for _ in range(T):
    N, M, K = map(int, input().split())
    G = [[] for i in range(N)]
    DP = [[False for i in range(2*K+1)] for j in range(N)]
    S = input()
    for i in range(M):
        U, V = map(int, input().split())
        G[U-1].append(V-1)

    for i in range(N):
        if S[i] == 'A':
            DP[i][2*K] = True
        else:
            DP[i][2*K] = False

    for step in range(2*K-1, -1, -1):
        if step % 2 == 0:
            currentTurn = True
        else:
            currentTurn = False
        
        for v in range(N):
            DP[v][step] = not currentTurn
            for u in G[v]:
                if currentTurn == DP[u][step+1]:
                    DP[v][step] = currentTurn
                    break

    if DP[0][0] == True:
        print('Alice')
    else:
        print('Bob')
