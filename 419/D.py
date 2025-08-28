N, M = map(int, input().split())
S = input()
T = input()
diff = [0] * (N+2)
for i in range(M):
    L, R = map(int, input().split())
    diff[L-1] += 1
    diff[R] -= 1

ans = ['']
curr = 0
for i in range(N+2):
    if (i >= 1) and (i <= N):
        if curr % 2 == 0:
            ans.append(S[i-1])
        else:
            ans.append(T[i-1])
    curr += diff[i]

print(''.join(ans))