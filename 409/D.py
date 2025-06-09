for test_case in range(int(input())):
    N = int(input())
    S = input()

    l = 0
    r = 0

    for i in range(N-1):
        if S[i] > S[i+1]:
            l = i
            break
    
    r = -1
    for j in range(l+1, N):
        if S[l] < S[j]:
            r = j-1
            break
    
    if r == -1:
        r = N-1

    print(S[0:l] + S[l+1:r+1] + S[l] + S[r+1:N])