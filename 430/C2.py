import bisect

N, A, B = map(int, input().split())
S = input().strip()

prefix_a = [0]
prefix_b = [0]

for ch in S:
    prefix_a.append(prefix_a[-1] + (ch == 'a'))
    prefix_b.append(prefix_b[-1] + (ch == 'b'))

ans = 0

if N == 1:
    if prefix_a[1] >= A and prefix_b[1] < B:
        ans = 1
else:
    for l in range(1,N + 1):
        target_a = prefix_a[l-1] + A
        target_b = prefix_b[l-1] + B

        a_i = bisect.bisect_left(prefix_a, target_a, l)
        b_i = bisect.bisect_left(prefix_b, target_b, l) - 1

        if a_i <= b_i and a_i <= N:
            ans += (b_i - a_i + 1)

print(ans)