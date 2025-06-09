N = int(input())
line = input()
A = list(map(int, line.split(' ')))
A_sorted = sorted(A)
A_res = []

for i in range(0,N-1):
    if (A_sorted[i] != A_sorted[i+1]):
        A_res.append(A_sorted[i])

A_res.append(A_sorted[N-1])
print(len(A_res))
for a in A_res:
    print(str(a) + ' ', end="")