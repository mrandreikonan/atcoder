X, Y = map(int, input().split())
if X+Y <= 12:
    ans = X+Y
else:
    ans = X + Y - 12

print(ans)