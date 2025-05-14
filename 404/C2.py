import sys

"""file = open('C_input.txt', 'r')
text = file.read()
lines=text.split('\n')
file.close()
n, m = lines[0].split(' ')
n = int(n)
m = int(m)"""

sizes = input()
n, m = sizes.split(' ')
n = int(n)
m = int(m)

v = [[] for i in range(0,n)]
visit = [False for i in range(0,n)]
visitCount = 0

"""for edge in lines[1:len(lines)]:
    A, B = edge.split(' ')
    A = int(A)
    B = int(B)
    v[A-1].append(B-1)
    v[B-1].append(A-1)"""

for line in range(0,m):
    edge = input()
    A, B = edge.split(' ')
    A = int(A)
    B = int(B)
    v[A-1].append(B-1)
    v[B-1].append(A-1)

def walk():
    current = 0
    visit[current] = True
    visitCount = 1

    for i in range(1,n):
        next = v[current][0]
        if False == visit[next]:
            visit[next] = True
            current = next
        else:
            next = v[current][1]
            if False == visit[next]:
                visit[next] = True
                current = next
            else:
                # no further moves. Check if came to start one
                if 0 in v[current]:
                    return True
                else:
                    return False

# Perfrom fast checks
# 1. Number of edges should be equal to number of vertices
if n != m:
    print('No\n')
    sys.exit()

# 2. Each vertice should have just 2 edges
for ver in v:
    if len(ver) != 2:
        print('No\n')
        sys.exit()

# Now walk through the graph
if False == walk():
    print('No\n')
else:
    print('Yes\n')