import sys

T = int(input())
for _ in range(T):
    TSx, TSy, TGx, TGy = map(int, input().split())
    ASx, ASy, AGx, AGy = map(int, input().split())

    m1 = (TGy - TSy) / (TGx - TSx)
    m2 = (AGy - ASy) / (AGx - ASx)

    Tx = TSx
    Ty = TSy
    Ax = ASx
    Ay = ASy

    ans = -1
    prev_dist = sys.maxsize

    for step in range(max(abs(TGx-TSx), abs(AGx-ASx)) + 1):
        if Tx != TGx or Ty != TGy:
            Tx = Tx + step
            Ty = TSy + m1 * (Tx - TSx)

        if Ax != AGx or Ay != AGy:
            Ax = Ax + step
            Ay = ASy + m1 * (Tx - TSx)

        dist = ((Tx-Ax)**2 + (Ty-Ay)**2) ** 0.5

        if dist < prev_dist:
            ans = dist
            prev_dist = dist
        else:
            ans = prev_dist
            break

    print(ans)

    dT = ((TGx-TSx)**2 + (TGy-TSy)**2) ** 0.5
    dA = ((AGx-ASx)**2 + (AGy-ASy)**2) ** 0.5