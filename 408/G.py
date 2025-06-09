import math

for test in range(int(input())):
    A, B, C, D = map(int, input().split())
    l = 1
    r = 10**18
    mid = (l + r) // 2

    while l < r:

        check_l = math.ceil(A * mid / B + 1e-9)
        check_r = math.floor(C * mid / D - 1e-9)

        if (check_l <= check_r):
            r = mid
        else:
            l = mid + 1
   
        mid = (l + r) // 2

    print(mid)
    