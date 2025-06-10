N, L = map(int, input().split())
d = list(map(int, input().split()))
cnt = [0]*L
cnt[0] = 1
sum = 0
ans = 0

for pnt in d:
    offset = (sum + pnt) % L
    sum += pnt
    cnt[offset] += 1

if L % 3 == 0:
    for pnt in range(L // 3):
        ans += cnt[pnt] * cnt[pnt + L // 3] * cnt[pnt + 2 * L // 3]

print(ans)