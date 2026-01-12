N = int(input())

a = [[0] * 2002 for _ in range(2002)]
b = [[0] * 2002 for _ in range(2002)]

for i in range(1, N+1):
    u, d, l, r = map(int, input().split())
    
    r += 1
    d += 1

    a[u][l] += 1
    a[u][r] -= 1
    a[d][l] -= 1
    a[d][r] += 1

    b[u][l] += i
    b[u][r] -= i
    b[d][l] -= i
    b[d][r] += i

for row in range(1, 2002):
    for col in range(1, 2002):
        a[row][col] += a[row][col-1]
        b[row][col] += b[row][col-1]

for col in range(1, 2002):
    for row in range(1, 2002):
        a[row][col] += a[row-1][col]
        b[row][col] += b[row-1][col]

cover = [0]*(N+1)

for row in range(1,2001):
    for col in range(1,2001):
        if a[row][col] == 0:
            cover[0] += 1
        elif a[row][col] == 1:
            cover[b[row][col]] += 1

for i in range(1, N+1):
    print(cover[0] + cover[i])