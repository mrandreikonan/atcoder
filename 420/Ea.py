from atcoder.dsu import DSU

N, Q = map(int, input().split())

dsu = DSU(N)
black_count = [0] * N
color = [0] * N

for _ in range(Q):
    query = input().split()
    if query[0] == '1':
        u = int(query[1]) - 1
        v = int(query[2]) - 1

        if False == dsu.same(v, u):
            u_black = black_count[dsu.leader(u)]
            v_black = black_count[dsu.leader(v)]

            black_count[dsu.leader(u)] = 0
            black_count[dsu.leader(v)] = 0

            dsu.merge(v, u)

            black_count[dsu.leader(v)] = u_black + v_black

    elif query[0] == '2':
        v = int(query[1]) - 1

        if color[v] == 0:
            black_count[dsu.leader(v)] += 1
            color[v] = 1
        else:
            black_count[dsu.leader(v)] -= 1
            color[v] = 0

    else:
         v = int(query[1]) - 1
         if black_count[dsu.leader(v)] > 0:
             print('Yes')
         else:
             print('No')