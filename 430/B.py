N, M = map(int, input().split())
S = [[0 for i in range(N)] for i in range(N)]
D = [[False for i in range(N)] for i in range(N)]
for i in range(N):
    s = input()
    for j in range(N):
        if s[j] == '#':
            S[i][j] = 1
        else:
            S[i][j] = 0

ans = 0

for i in range(N - M + 1):
    for j in range(N - M +1):

        if D[i][j] == True:
            continue
        else:
            D[i][j] = True
            ans += 1

        for k in range(N - M + 1):
            for l in range (N - M + 1):
               
                diff = False

                for ii in range(M):
                    for jj in range(M):
                        if S[i+ii][j+jj] != S[k+ii][l+jj]:
                            diff = True
                            break
                    if diff == True:
                        break
                
                if diff == False:
                    D[k][l] = True

print(ans)