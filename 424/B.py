N, M, K = map(int, input().split())
solved = [0]*N
ans = []
for _ in range(K):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    solved[a] += 1
    if solved[a] == M:
        ans.append(a+1)

for an in ans:
    print(an, end='')
    print(' ', end='')
print();
