S = input()
ans = ""
for i in range(len(S)):
    if i != (len(S) // 2):
        ans += S[i]
print(ans)