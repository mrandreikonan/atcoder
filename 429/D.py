import bisect

N, M, C = map(int, input().split())
A = list(map(int, input().split()))
A = sorted(A)

P = []
S = []
s = 0
ans = 0

for j in range(2):
    Pcount = 1
    Ploc = A[0]
    s += 1

    for i in range(1,N):
        if A[i] == Ploc:
            Pcount += 1
            s += 1            
        else:
            P.append((Pcount, j*M+Ploc))
            S.append(s)
            Pcount = 1
            Ploc = A[i]
            s += 1

        if i == N-1:
            P.append((Pcount, j*M+Ploc))
            S.append(s)

m = 0.5
loc_prev = 0

if N == 1:
     print(M)
else:
    if P[0][1] == 0:
        search_idx = 1
        S_prev = P[0][0]
    else:
        search_idx = 0
        S_prev = 0


    while m < M:
        # find next S from search_idx to equal or greater to S[prev] + C
        idx = bisect.bisect_left(S, S_prev + C, lo = search_idx)
        t = S[idx] - S_prev
        mt = t * (min(P[search_idx][1], M) - loc_prev)
        ans += mt

        m = P[search_idx][1] + 0.5
        loc_prev = P[search_idx][1]
        S_prev = S[search_idx]

        search_idx += 1

    print(ans)