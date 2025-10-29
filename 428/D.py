T = int(input())

perf_squares = []
for i in range(84852):
    perf_squares.append(i*i)

for _ in range(T):
    C, D = map(int, input().split())
    ans = 0

    for ps in perf_squares:
        for i in range(10):
            if ps > 2*C + i*C:
                ans += 1

    print(ans)