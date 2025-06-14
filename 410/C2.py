N, Q = map(int, input().split())

A = [0]
for i in range(N):
    A.append(i+1)

cum_shift = 0

for query in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        if q[1] > cum_shift:
            orig_pos = q[1] - cum_shift
        else:
            orig_pos = N - (abs(q[1] - cum_shift) % N)
        A[orig_pos] = q[2]
    elif q[0] == 2:
        new_pos = (q[1] + cum_shift) % N
        print(A[new_pos])
    else:
        cum_shift += q[1]