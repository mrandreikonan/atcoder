from collections import deque

N, Q = map(int, input().split())
S = [0] * (N+1)
ver = [(-1,'')]

for _ in range(Q):
    q = input().split()
    if int(q[0]) == 1:
        S[int(q[1])] = S[0]
    elif int(q[0]) == 2:
        v_old = ver[S[int(q[1])]]
        v_new = (S[int(q[1])], q[2])
        ver.append(v_new)
        S[int(q[1])] = len(ver) - 1
    else:
        S[0] = S[int(q[1])]

v = ver[S[0]]
dq = deque()

while (v[0] != -1):
    dq.appendleft(v[1])
    v = ver[v[0]]

print("".join(dq))