N, Q = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sum = 0
for i in range(N):
    sum += min(A[i], B[i])

for i in range(Q):
    newAx = newBx = 0
    
    query = input().split()
    X = int(query[1]) - 1
    V = int(query[2])

    if query[0] == 'A':
        newAx = V
        newBx = B[X]
    else:
        newAx = A[X]
        newBx = V

    sum -= min(A[X], B[X])
    sum += min(newAx, newBx)
    A[X] = newAx
    B[X] = newBx

    print(sum)