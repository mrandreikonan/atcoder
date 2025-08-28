N = int(input())
L = U = 1000000001
R = D = -1
for i in range(N):
    row, col = map(int,input().split())
    if row < U:
        U = row
    if row > D:
        D = row
    if col < L:
        L = col
    if col > R:
        R = col

col_dist = R-L+1
row_dist = D-U+1

print(max(col_dist // 2, row_dist // 2))