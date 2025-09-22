X, C = map(int, input().split())
ans = X*1000 // (1000 + C)
res = ans % 1000
print(ans - res)