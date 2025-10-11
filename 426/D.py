T = int(input())
for _ in range(T):
    N = int(input())
    S = input()

    num_zero = 0
    num_one = 0
    max_run = [0, 0]

    for i in range(N):
        if int(S[i]) == 0:
            num_zero +=1
        else:
            num_one +=1

    run_start = [-1, -1]

    prev = int(S[0])
    run_start[prev] = 0

    for j in range(1, N):
        if prev != int(S[j]):
            max_run[prev] = max(max_run[prev], j - run_start[prev])
            prev = int(S[j])
            run_start[prev] = j
    
    max_run[prev] = max(max_run[prev], N - run_start[prev])

    ans_to_zero = num_one + 2 * (num_zero - max_run[0])
    ans_to_one = num_zero + 2 * (num_one - max_run[1])

    print(min(ans_to_zero, ans_to_one))
