from functools import cmp_to_key

import bisect

def compare(x, y):    
    if x[0] < y[0]:
        return -1
    elif x[0] > y[0]:
        return 1
    else:
        return 0

#with open("E_input.txt", 'r') as f:
#    lines = [line.strip() for line in f.readlines()]

T = int(input())
#T = int(lines[0])
test_results = []

for t in range(0,T):
    N = int(input())
    #N = int(lines[1])
    A = []
    for a in range(0, 2*N):
        #A.append([int(lines[2 + a]), a])
        A.append([int(input()), a])

    A_sorted = sorted(A, key = cmp_to_key(compare))

    ans = []
    val = []
    while len(ans) < N:
        p = A_sorted.pop()
        
        # Check if it is possible to put open brace in max_idx
        b_index = bisect.bisect_left(ans, p[1])
        braces_after = len(ans) - b_index

        left_space = 2 * N - p[1] - 1 - 2 * braces_after

        if (left_space > 0) and (p[1] != 2*N -1):
            bisect.insort(ans, p[1])
            val.append(p[0])

    test_results.append(sum(val))

for rs in test_results:
    print(rs)
