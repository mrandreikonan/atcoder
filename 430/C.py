N, A, B = map(int, input().split())
S = input()

ans = 0

for i in range(N):
    for j in range(i,N):

        if i == j:
            if S[i] == 'a':
                a_cnt = 1
                b_cnt = 0
            else:
                a_cnt = 0
                b_cnt = 1

        if a_cnt >= A and b_cnt < B:
            ans += 1

        if (j != N-1):
            if S[j+1] == 'a':
                a_cnt += 1
            else:
                b_cnt += 1

        if b_cnt >= B:
            break
    
print(ans)