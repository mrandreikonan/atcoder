from atcoder.segtree import SegTree
import sys

input = sys.stdin.readline

N, D, R = map(int, input().split())
H = [0] + list(map(int, input().split()))

ans = [0] * (N+1)
pos = [0] * (N+1)

for i in range(1, N+1):
    pos[H[i]] = i

SegT = SegTree(max, -1, [-1] * (N+1))

for i in range(1, N+1):
    ps = pos[i]
    if i >= D + 1:
        SegT.set(pos[i-D], ans[i-D])
   
    ans[i] = SegT.prod(max(1, ps - R), min(N, ps + R + 1)) + 1

    #print(ans)
    #print([SegT.get(j) for j in range(N+1)])

print(max(ans))