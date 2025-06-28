S = input()
T = input()

ans = True

for i in range(1,len(S)):
    if S[i].isupper():
        if S[i-1] not in T:
            ans = False
            break

if ans == True:
    print('Yes')
else:
    print('No')