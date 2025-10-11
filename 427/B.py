N = int(input())
A = [0]*(N+1)
A[0] = 1
A[1] = 1

def f(n):
    res = 0
    while n > 0:
        res += n % 10
        n = n // 10
    return res

for i in range(2, N+1):
    A[i] = A[i-1] + f(A[i-1])

print(A[N])