N = int(input())
D = list(map(int, input().split()))

for i in range(0,N-1):
    for j in range(i+1,N):
        dist = 0
        for d in range(i,j):
            dist += D[d]
        print(str(dist) + ' ', end="")
    print()