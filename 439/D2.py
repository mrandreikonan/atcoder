N = int(input())
A = list(map(int, input().split()))


count3 = {}
count7 = {}

for el in A:
    if el % 3 == 0:
        t = el // 3
        if t in count3:
            count3[t] += 1
        else:
            count3[t] = 1

    if el % 7 == 0:
        t = el // 7
        if t in count7:
            count7[t] += 1
        else:
            count7[t] = 1

ans = 0

for el in A:
    if el % 5 == 0:
        t = el // 5
        if t in count3 and t in count7:
            ans += count3[t] * count7[t]
    
    if el % 3 == 0:
        t = el // 3
        count3[t] -= 1

    if el % 7 == 0:
        t = el // 7
        count7[t] -= 1

count3.clear()
count7.clear()

for el in reversed(A):
    if el % 3 == 0:
        t = el // 3
        if t in count3:
            count3[t] += 1
        else:
            count3[t] = 1

    if el % 7 == 0:
        t = el // 7
        if t in count7:
            count7[t] += 1
        else:
            count7[t] = 1

for el in reversed(A):

    if el % 5 == 0:
        t = el // 5
        
        if t in count3 and t in count7:
            ans += count3[t] * count7[t]
    
    if el % 3 == 0:
        t = el // 3
        count3[t] -= 1

    if el % 7 == 0:
        t = el // 7
        count7[t] -= 1

print(ans)