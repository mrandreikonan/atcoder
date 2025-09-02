N = int(input())
S = []
for i in range(N):
    s = input()
    S.append(s)
X, Y = input().split()
room = int(X) - 1

found = False

for i in range(N):
    if i == room and S[i] == Y:
        found = True
        break

if True == found:
    print('Yes')
else:
    print('No')