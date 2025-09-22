from collections import deque

N = int(input())

skills = deque()
learned = [0]*N
enable = []
ans = 0

for i in range(N):
    enable.append([])

for i in range(N):
    A, B = map(int, input().split())
    enable.append([])
    if (A == 0) and (B == 0):
        learned[i] = 1
        ans += 1
        skills.append(i)
    else:
        A -= 1
        B -= 1
        enable[A].append(i)
        enable[B].append(i)

while len(skills) > 0:
    skill = skills.popleft()
    for i in range(len(enable[skill])):
        if learned[enable[skill][i]] == 0:
            learned[enable[skill][i]] = 1
            ans += 1
            skills.append(enable[skill][i])

print(ans)