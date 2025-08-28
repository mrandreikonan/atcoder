import heapq

Q = int(input())
heap = []

for i in range(Q):
    q = list(map(int,input().split()))
    if (q[0] == 1):
        heapq.heappush(heap,q[1])
    else:
        print(heapq.heappop(heap))