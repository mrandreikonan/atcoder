line = input()
X, Y = line.split(' ')
X = int(X)
Y = int(Y)

R = []

for d1 in range(1,7):
    for d2 in range(1,7):
        n = 10*d1 + d2
        if (d1+d2) >= X:            
            if n not in R:
                R.append(n)
        if abs(d1-d2) >= Y:
            if n not in R:
                R.append(n)

ans = float(len(R)) / float(36)
print(ans)