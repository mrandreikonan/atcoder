good = {}
for i in range(1,3165):
    for j in range(i+1, 3165):
        n = i*i + j*j
        if n <= 10000000:
            if n in good:
                good[n] += 1
            else:
                good[n] = 1
        else:
            break

N = int(input())

ans = []

for i in good.keys():
    if i <= N and good[i] == 1:
        ans.append(i)

ans.sort()

print(len(ans))
for a in ans:
    print(a, end="")
    print(" ", end="")
print()