S, A, B, X = map(int, input().split())
ans = 0
while (X > 0):
    if X <= A:
        ans += X * S
        X -= A
        break
    else:
        ans += A * S
        X -= A

    if X <= B:
        X -= B
        break
    else:
        X -= B
print(ans)