N, M = map(int, input().split())
E = []
ans = M + 1

for i in range(M):
    u, v = map(int, input().split())
    E.append((u-1,v-1))

for number in range(pow(2,N)-1):
    res = 0
    for e in E:
        u = e[0]
        v = e[1]
        c_u = (number & (1 << u)) >> u
        c_v = (number & (1 << v)) >> v
        if c_u == c_v:
           res += 1 
    
    if res < ans:
        ans = res

print(ans)