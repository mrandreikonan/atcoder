T = int(input())

for _ in range(T):
    N, H = map(int, input().split())
    course = []
    for i in range(N):
        t, l, u = map(int, input().split())
        course.append((t,l,u))
    
    ans = True
    cur = (0, H, H)
    for i in range(N):
        t, l, u = course[i]
        L = max(1, cur[1] - (t-cur[0]))
        U = cur[2] + (t-cur[0])

        # compare (l,u) and (L,U) ranges overlap
        if max(l,L) > min(u,U):
            ans = False
            break
        else:
            cur = (t, max(l,L), min(u,U))
        
    if ans == True:
        print('Yes')
    else:
        print('No')   