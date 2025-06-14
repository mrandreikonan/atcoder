N, Q = map(int, input().split())
X = list(map(int, input().split()))
ball = [0]*N
B = []

for x in X:
    if x > 0:
        ball[x-1] += 1
        B.append(x)
    else:
        mn = 1000
        ps = 0
        for i in range(N):
            if ball[i] < mn:
                mn = ball[i]
                ps = i
        ball[ps] += 1
        B.append(ps + 1)

print(' '.join(map(str, B)))