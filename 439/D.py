import bisect

N = int(input())
A = list(map(int, input().split()))
P = [(value, index) for index, value in enumerate(A)]


P.sort()

prev = -1
ans = 0

for index in range(len(P)):
    i = P[index][0]
    i_idx = index

    if i == prev:
        continue
    else:
        prev = i

    # j / i = 5 / 3 => j = 5 * i / 3

    j = 5 * i / 3
    k = 7 * i / 3

    if False == j.is_integer() or False == k.is_integer():
        continue

    j_idx = bisect.bisect_left(P, (j, 0), index+1)
    k_idx = bisect.bisect_left(P, (k, 0) , index+1)

    if not (j_idx < N and P[j_idx][0] == j and k_idx < N and P[k_idx][0] == k):
        continue

    for jj in range(j_idx, N):
        if P[jj][0] == j:
            j_pos = P[jj][1]

            i_max_pos = bisect.bisect_left(P, (i, j_pos), i_idx)
            i_cnt = i_max_pos - i_idx + 1

            k_max_pos = bisect.bisect_left(P, (k, j_pos), k_idx)
            k_cnt = k_max_pos - k
            
            ans += i_cnt * k_cnt

            

        else:
            break

    for ii in range(i_idx, N):
        if P[ii][0] == i:
            for jj in range(j_idx, N):
                if P[jj][0] == j:
                    for kk in range(k_idx, N):
                        if P[kk][0] == k:
                            # ratio is good, check min/max
                            if min(P[ii][1], P[jj][1], P[kk][1]) == P[jj][1] or max(P[ii][1], P[jj][1], P[kk][1]) == P[jj][1]:
                                ans += 1
                        else:
                            break
                else:
                    break
        else:
            break

print(ans)