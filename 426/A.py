X, Y = input().split()

if X == 'Ocelot':
    x = 1
elif X == 'Serval':
    x = 2
else:
    x = 3

if Y == 'Ocelot':
    y = 1
elif Y == 'Serval':
    y = 2
else:
    y = 3

if x >= y:
    print('Yes')
else:
    print('No')