import bisect

T = int(input())
for _ in range(T):
    N = int(input())
    S = list(map(int, input().split()))
    S[1:-1] = sorted(S[1:-1])
    
    ans = -1
    first = S[0]
    last = S[-1]

    if (len(S) == 2):
        if S[1] > 2 * S[0]:
            print('-1')
        else:
            print('2')
    else:
        ans = 0
        srchF = 1
        srchL = len(S)-1
        current = first
        while (2 * current < last):
            ind = bisect.bisect_right(S, 2 * current, srchF, srchL)
            if ind == srchF:
                ans = -1
                break
            else:
                current = S[ind-1]
                srchF = ind
                ans += 1
        
        if ans != -1:
            ans += 2    
        
        print(ans)

        
