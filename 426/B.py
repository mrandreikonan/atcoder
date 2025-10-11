S = input()

for i in range(len(S)):
    ch = S[i]
    diff = True
    for j in range(len(S)):
        if i == j:
            continue
        if S[i] == S[j]:
            diff = False
            break
    if diff == True:
        print(ch)
        break