N, R = map(int, input().split())
L = list(map(int, input().split()))

ans = 0

LL = 0
RR = N -1

while LL < R and L[LL] == 1:
    LL += 1

while RR >= R and L[RR] == 1:
    RR -= 1

for i in range(LL,RR+1):
    if L[i] == 0:
        ans += 1
    else:
        ans += 2

print(ans)