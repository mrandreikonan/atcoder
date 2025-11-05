from collections import deque
A = deque()

Q = int(input())
for _ in range(Q):
    q = input().split()
    if q[0] == '1':
        A.append((int(q[2]), int(q[1])))
    else:
        k = int(q[1])
        ans = 0
        while k > 0:
            el = A[0]
            if el[1] <= k:
                ans += el[0] * el[1]
                A.popleft()
                k -= el[1]
            else:
                A[0] = (el[0], el[1] - k)
                ans += k * el[0]
                k = 0
        print(ans)