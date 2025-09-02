N = int(input())
S = input()
order1 = []
order2 = []
for i in range(0, N):
    order1.append(2*i)
    order2.append(1 + 2*i)
curr = []
for i in range(0,len(S)):
    if S[i] == 'A':
        curr.append(i)
ans = [0, 0]
for i in range(N):
    ans[0] += abs(curr[i] - order1[i])
    ans[1] += abs(curr[i] - order2[i])

print(min(ans))