import sys
input = sys.stdin.readline

#import os
#script_dir = os.path.dirname(os.path.abspath(__file__))
#file_path = os.path.join(script_dir, 'input_E_3.txt')
#file = open(file_path, 'r')
#text = file.read()
#lines=text.split('\n')
#N = int(lines[0])
#X = list(map(int, lines[1].split()))

N = int(input())
X = list(map(int,input().split()))

G = [[] for _ in range(N)]
C = [0] * N

for edge in range(N-1):
    u, v, w = map(int, input().split())
    #u, v, w = map(int, lines[2+edge].split())
    G[u-1].append([v-1, w, False])
    G[v-1].append([u-1, w, False])
    C[u-1] += 1
    C[v-1] += 1

ans = 0
moved = 0

pool_idx = 0
pool = []

# Find leaves
for v in range(N):
    if C[v] == 1:
        pool.append(v)

while moved < N - 1:
    
    pool_sz = len(pool)
    # Move charge from leaves
    for i in range(pool_idx, pool_sz):
        v = pool[i]
        u = w = -1
        used = False

        for j in range(len(G[v])):
            if G[v][j][2] == True:
                continue
            else:
                u = G[v][j][0]
                w = G[v][j][1]
                G[v][j][2] = True
                break

        ans += abs(X[v]) * w
        X[u] += X[v]
        X[v] = 0

        C[u] -= 1
        C[v] -= 1
        moved += 1

        if C[u] == 1:
            pool.append(u)

        if moved == N - 1:
            break
        
        pool_idx += 1

print(ans)