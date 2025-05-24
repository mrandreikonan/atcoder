line = input()
A, B = line.split(' ')
A = int(A)
B = int(B)

ans = 0
diff = 10004

for i in range(0,500):
    drob = (float(A) / float(B))
    if drob > i:
        df =  drob - i
    else:
        df = i - drob

    if (df < diff):
        diff = df
        ans = i

print(ans)