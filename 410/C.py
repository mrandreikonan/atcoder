
from collections import deque

N, Q = map(int, input().split())

A = deque([])
for i in range(N):
    A.append(i+1)

for query in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        A[q[1] - 1] = q[2]
    elif q[0] == 2:
        print(A[q[1] - 1])
    else:
        for i in range(q[1]):
            el = A.popleft()
            A.append(el)