G = [0]
MAX_N = 8
ans = 1000000000
U = [False] * MAX_N
P = [0] * MAX_N

def AddEdge(G, A, B):
    minA = min(A,B)
    maxB = max(A,B)
    bit_offset = 0
    for block in range(minA):
        bit_offset += MAX_N - block - 1
    bit_offset += maxB - minA
    G[0] |= (1 << bit_offset)

N, M = map(int, input().split())
for _ in range (M):
    A, B = map(int, input().split())
    AddEdge(G, A-1, B-1)

def perm(P, first_comp_size, pos):
    global ans
    if pos == N:
        G1 = [0]
        for v in range(first_comp_size-1):
            AddEdge(G1, P[v], P[v+1])
        AddEdge(G1, P[first_comp_size-1], P[0])

        G2 = [0]
        if first_comp_size != N:
            for v in range(first_comp_size, N-1):
                AddEdge(G2, P[v], P[v+1])
            AddEdge(G2, P[N-1], P[first_comp_size])

        G3 = [G1[0] | G2[0]]

        diff = bin(G3[0] ^ G[0]).count('1')
        if diff < ans:
            ans = diff
    else:
        for v in range(0, N):
            if U[v] == True:
                continue
            else:
                P[pos] = v
                U[v] = True
                perm(P, first_comp_size, pos + 1)
                U[v] = False

# Two components
first_comp_size = [[],[],[],[3],[4],[5],[3,6],[3,4,7],[3,4,5,8]]
for comp_size in first_comp_size[N]:
    perm(P, comp_size, 0)

print(ans)
