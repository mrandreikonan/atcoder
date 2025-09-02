# Based on logic from https://atcoder.jp/contests/abc421/submissions/69006037

Rt, Ct, Ra, Ca = map(int, input().split())
N, M, L = map(int, input().split())
S = [0]*M
T = [0]*L

def getMove(direction):
    #RDLU
    move = [(0,1), (1,0), (0,-1), (-1,0)]
    if direction == 'R':
        return move[0]
    elif direction == 'D':
        return move[1]
    elif direction == 'L':
        return move[2]
    else:
        return move[3]

for i in range(M):
    dir, steps = input().split()
    S[i] = (getMove(dir), int(steps))
for i in range(L):
    dir, steps = input().split()
    T[i] = (getMove(dir), int(steps))

curS = S[0]
curT = T[0]
processedLen = 0
curSi = 0
curTi = 0

s = []
t = []

#for i in range(max(M,L)):
while processedLen < N:
    minSteps = min(curS[1], curT[1])
    s.append((curS[0], minSteps))
    t.append((curT[0], minSteps))
    processedLen += minSteps

    curS = (curS[0], curS[1] - minSteps)
    curT = (curT[0], curT[1] - minSteps)

    if curS[1] == 0 and curSi < M - 1:
        curSi += 1
        curS = S[curSi]

    if curT[1] == 0 and curTi < L - 1:
        curTi += 1
        curT = T[curTi] 

ans = 0

Tpos = (Rt, Ct)
Apos = (Ra, Ca)

for i in range(len(s)):
    Tdir, Tcnt = s[i]
    Adir, Acnt = t[i]
    m = min(Tcnt, Acnt)

    dr, dc = Tdir
    dR, dC = Adir

    if Tdir == Adir:
        if Tpos == Apos:
            ans += m
    else:
        x1 = x2 = float('inf')
        if dr - dR != 0 and dc - dC != 0:
            if (Apos[0] - Tpos[0]) % (dr - dR) == 0 and (Apos[1] - Tpos[1]) % (dc - dC) == 0:
                x1 = (Apos[0] - Tpos[0]) // (dr - dR)
                x2 = (Apos[1] - Tpos[1]) // (dc - dC)
        elif dr - dR != 0:
            if (Apos[0] - Tpos[0]) % (dr - dR) == 0:
                x1 = x2 = (Apos[0] - Tpos[0]) // (dr - dR)
        elif dc - dC != 0:
            if (Apos[1] - Tpos[1]) % (dc - dC) == 0:
                x1 = x2 = (Apos[1] - Tpos[1]) // (dc - dC)

        if 0 < x1 == x2 <= m:
            Tp = (Tpos[0] + dr * x1, Tpos[1] + dc * x1)
            Ap = (Apos[0] + dR * x1, Apos[1] + dC * x1)
            if Tp == Ap:
                ans += 1

    Tpos = (Tpos[0] + dr * m, Tpos[1] + dc * m)
    Apos = (Apos[0] + dR * m, Apos[1] + dC * m)

print(ans)