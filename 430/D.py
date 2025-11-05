from sortedcontainers import SortedList
import bisect
import sys
input = sys.stdin.readline

N = int(input())
x = list(map(int, input().split()))
D = [0]*(N+1)

X = SortedList([])
X.add((0,x[0]))
X.add((x[0],x[0]))
S = 2 * x[0]
print(S)

for i in range(1,N):
    idx = X.bisect_left((x[i], 0))
    l = x[i] - X[idx-1][0]

    if idx == len(X):
        r = sys.maxsize
    else:
        r = X[idx][0] - x[i]

    if X[idx-1][1] > l:
       S -= X[idx-1][1] - l
       old = X.pop(idx-1)
       X.add((old[0], l))

    if r != sys.maxsize and X[idx][1] > r:
       S -= X[idx][1] - r
       old = X.pop(idx)
       X.add((old[0], r))
       
    
    X.add((x[i],min(l, r)))
    S += X[idx][1]

    print(S)