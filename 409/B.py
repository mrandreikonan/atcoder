N = int(input())
A = map(int, input().split())
As = sorted(A, reverse = True)

pos = 0
ans = 1

for i in range(1,N):
    if As[i] == As[i-1]:
        continue

    if (i >= As[i-1]):
        

print(ans)