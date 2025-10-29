Q = int(input())

balance = []
min_balance = []

for _ in range(Q):
    query = input().split()

    if len(balance) == 0:
        new_balance = 0
    else:
        new_balance = balance[-1]

    if query[0] == '1':      
        if query[1] == '(':
            new_balance += 1
        else:
            new_balance -= 1
        balance.append(new_balance)
        if len(min_balance) > 0:
            min_balance.append(min(min_balance[-1], new_balance))
        else:
            min_balance.append(new_balance)
    else:
        balance.pop()
        min_balance.pop()

    if (len(balance) == 0) or (balance[-1] == 0 and min_balance[-1] >= 0):
        print('Yes')
    else:
        print('No')