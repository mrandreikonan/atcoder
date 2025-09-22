# Based on https://atcoder.jp/contests/abc424/submissions/69500897
import heapq
from collections import Counter

T = int(input())
for _ in range(T):
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))

    counter = Counter(A)

    max_heap = [(-n, cnt) for n, cnt in counter.items()]
    heapq.heapify(max_heap)

    total = N
    while K > 0:
        n, cnt = heapq.heappop(max_heap)
        n = -n

        todo = min(cnt, K)
        left = cnt - todo

        if left > 0:
            heapq.heappush(max_heap, (-n, left))

        heapq.heappush(max_heap, (-(n/2), 2 * todo))

        K -= todo
        total += todo
    
    ans = 0.0
    while(max_heap):
        n, cnt = heapq.heappop(max_heap)
        n = -n
        if X <= cnt:
            ans = n
            break
        X -= cnt

    print(ans)