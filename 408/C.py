line = input()
N, M = line.split(' ')
N = int(N)
M = int(M)
hit = [0 for idx in range(0,N+1)]
hit[0] = 1000000

for i in range(0,M):
    line = input()
    L, R = line.split(' ')
    L = int(L)
    R = int(R)
    for i in range(L,R+1):
        hit[i] += 1

print(min(hit))