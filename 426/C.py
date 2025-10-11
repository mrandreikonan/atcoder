import heapq

N, Q = map(int, input().split())
V = [(i,1) for i in range(1, N+1)]

heapq.heapify(V)

for _ in range(Q):
    X, Y = map(int, input().split())

    ans = 0
    new_el_cnt = 0

    while V[0][0] <= X:
        el = heapq.heappop(V)     
        new_el_cnt += el[1]
        ans += el[1]

    heapq.heappush(V, (Y, new_el_cnt))
    print(ans)