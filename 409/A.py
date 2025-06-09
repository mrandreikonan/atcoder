N = int(input())
T = input()
A = input()

ans = False

for i in range(N):
    if T[i] == 'o' and A[i] == 'o':
        ans = True
        break

if True == ans:
    print('Yes')
else:
    print('No')