from heapq import*
for i in range(int(input())):
  q=[];r=0
  for i in range(int(input())):
    heappush(q,-int(input()))
    r-=heappop(q)
    heappush(q,-int(input()))
  print(r)