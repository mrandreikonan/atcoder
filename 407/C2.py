S = input()

ans = 0
minus = 0
it = len(S) - 1
next = S[it]

while it >= 0:
    last = int(next)
    ans += (last + 1)
    minus += last

    it -= 1
    if it < 0:
        break
  
    new_last = int(S[it])
    minus_mod = minus % 10
    if new_last >= minus_mod:
        new_last = new_last - minus_mod
    else:
        new_last = 10 + new_last - minus_mod
    
    next = str(new_last)


print(ans)