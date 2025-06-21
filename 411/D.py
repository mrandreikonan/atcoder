N, Q = map(int, input().split())
S = [0] * (N+1)
ver = ['']

for _ in range(Q):
    q = input().split()
    if int(q[0]) == 1:
        S[int(q[1])] = S[0]
    elif int(q[0]) == 2:
        v = ver[S[int(q[1])]]
        v += q[2]
        ver.append(v)
        S[int(q[1])] = len(ver) - 1
    else:
        S[0] = S[int(q[1])]

print(ver[S[0]])