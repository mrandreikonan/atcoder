S = input()
s = []

for i in range(len(S)):
    s.append(int(S[i]))

N = len(s)
ans = 0

for i in range(N-1):
    if s[i] + 1 == s[i+1]:
        ans += 1
        for j in range(0,min(i,N-i-2)):
            if (s[i-j-1] + 1 == s[i+j+2]) and (s[i-j-1] == s[i]):
                ans +=1
            else:
                break

print(ans)