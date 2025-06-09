N = int(input())
A = list(map(int, input().split()))

for ans in range(100,-1,-1):
    count = 0
    for a in A:
        if a >= ans:
            count += 1
    if count >= ans:
        break
print(ans)