line = input()
N, S = line.split(' ')
N = int(N)
S = int(S)
line = input()
T = [0] + list(map(int, line.split(' ')))

result = "Yes"

for t in range(1,N+1):
    if T[t] - T[t-1] > S:
        result = "No"
        break

print(result)