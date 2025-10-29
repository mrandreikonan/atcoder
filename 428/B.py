N, K = map(int, input().split())
S = input()
ans = []
ansCount = 0

for i in range(N-K+1):
    sub = S[i:i+K]

    count = 0
    for j in range(i,N-K+1):
        sub2 = S[j:j+K]
        if sub == sub2:
            count += 1

    if not sub in ans:
        if count > ansCount:
            ans = []
            ansCount = count
            ans.append(sub)
        elif count == ansCount:
            ans.append(sub)

ans = sorted(ans)
print(ansCount)
for ans_str in ans:
    print(ans_str + ' ', end="")
print()