X, Y = map(int, input().split())

def f(x):
    res = 0
    while x > 0:
        res = res * 10 + x % 10
        x = x // 10
    return res

a = [0] * 10
a[0] = X
a[1] = Y

for i in range(2,10):
    a[i] = f(a[i-1] + a[i-2])

print(a[9])