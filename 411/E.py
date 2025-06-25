import bisect
import atcoder.math
import math

N = int(input())
A = [] * N
S = []

for die in range(N):
    a = list(map(int, input().split()))
    A.append(a[:])
    for side in range(6):
        S.append(A[die][side])

S = sorted(set(S))
U = [[] for _ in range(len(S))]


for die in range(N):
    for side in range(6):
        id = bisect.bisect_left(S, A[die][side])
        U[id].append(die)

ans = 0
prod = 1
b = [0]*N
unrolled_cnt = N
MOD = 998244353

for i in range(len(S)-1):
    for die in U[i]:
        if (b[die] == 0):
            unrolled_cnt -= 1
        else:
            prod *= atcoder.math.inv_mod(b[die], MOD)
            prod %= MOD
            prod *=6
            prod %= MOD

        b[die] += 1
        prod *= b[die]
        prod %= MOD
        prod *= atcoder.math.inv_mod(6, MOD)
        prod %= MOD

    if (unrolled_cnt == 0):
        ans -= (S[i+1] - S[i]) * prod
        ans %= MOD

ans += S[len(S) - 1]
ans %= MOD

print(ans)