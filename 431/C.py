N, M, K = map(int, input().split())
H = list(map(int, input().split()))
B = list(map(int, input().split()))

H = sorted(H)
B = sorted(B)

ans = True

for i in range(K):
    h = H[i]
    b = B[M-K+i]
    if h > b:
        ans = False
        break

if ans == True:
    print('Yes')
else:
    print('No')