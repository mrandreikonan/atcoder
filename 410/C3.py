N, Q = map(int, input().split())

A = []
for i in range(N):
    A.append(i+1)

cum_shift = 0

for query in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        A[((q[1] - 1) + cum_shift) % N] = q[2]
    elif q[0] == 2:
        print(A[((q[1] - 1) + cum_shift) % N])
    else:
        cum_shift += q[1]
        cum_shift = cum_shift % N