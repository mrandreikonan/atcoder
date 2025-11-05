T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    A = sorted(A, key=abs, reverse = True)
    progression = True

    if abs(A[0]) == abs(A[-1]):
        below = above = 0
        for i in range(N):
            if A[i] < 0:
                below += 1
            else:
                above += 1
        
        if below == 0 or below == above or below - 1 == above or above - 1 == below:
            print('Yes')
            continue

    for i in range(2,N):
        if A[i] * A[i-2] != A[i-1] * A[i-1]:
            progression = False
            break
    if progression == True:
        print('Yes')
    else:
        print('No')