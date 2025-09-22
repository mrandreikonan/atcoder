import sys
import heapq
from collections import deque

queue = deque()

N, K = map(int, input().split())
for i in range(N):
    A, B, C = map(int, input().split())
    queue.append((A, B, C))

ans = []
R = []
rCount = 0
t = queue[0][0]

while len(queue) > 0:
    
    nextEnterT = max(queue[0][0], t)
        
    if len(R) > 0:
        nextExitT = R[0][0]
    else:
        nextExitT = sys.maxsize
    
    if (nextEnterT <= nextExitT) and (K - rCount >= queue[0][2]):
        heapq.heappush(R, (nextEnterT + queue[0][1], queue[0][2]))
        rCount += queue[0][2]
        queue.popleft()
        t = nextEnterT
        ans.append(t)
    else:
        t = nextExitT
        rCount -= R[0][1]
        heapq.heappop(R)

for i in range(N):
    print(ans[i])