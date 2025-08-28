N, M = map(int, input().split())
S = []
for i in range(N):
    S.append(input())

score = [0] * N

for i in range(M):
    x = y = 0
    for j in range(N):
        if S[j][i] == '0':
            x += 1
        else:
            y += 1
    
    if x == 0 or y == 0:
        for j in range(N):
            score[j] += 1
    elif (x < y):
        for j in range(N):
            if S[j][i] == '0':
                score[j] += 1
    elif (x > y):
        for j in range(N):
            if S[j][i] == '1':
                score[j] += 1

ans = []
max_score = max(score)
for i in range(N):
    if score[i] == max_score:
        ans.append(i+1)
ans = sorted(ans)
for index in ans:
    print(index, end='')
    if index == ans[-1]:
        print()
    else:
        print(' ', end='')