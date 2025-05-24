import sys

S = input()

ans = sys.maxsize

def walk(curS, curAns, incs):
    global S
    global ans

    if (len(curS) > len(S)) or (curAns > ans):
        return
    elif len(curS) == len(S):
        if (curS == S) and (curAns < ans):
            ans = curAns
            return
        else:
            # Press #2 one is not an option due to size
            plusS = ''
            for ch in curS:
                dig = int(ch)
                dig = (dig + 1) % 10
                plusS += str(dig)
            incs += 1
            if incs < 9:
                walk(plusS, curAns + 1, incs)
            else:
                return
    else:
        # Press button 1
        walk(curS + '0',curAns + 1,0)
        # Press button 2
        plusS = ''
        for ch in curS:
            dig = int(ch)
            dig = (dig + 1) % 10
            plusS += str(dig)
        incs += 1
        if incs < 9:
            walk(plusS, curAns + 1, incs)
        else:
            return

sys.setrecursionlimit(1000000000)
walk('0', 1, 0)
print(ans)