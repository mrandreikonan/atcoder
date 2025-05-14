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

def walk(vert):
    global visitCount
    global visit
    visit[vert] = True
    visitCount += 1

    v_one = v[vert][0]
    if visit[v_one] == False:
        walk(v_one)
    
    v_two = v[vert][1]
    if visit[v_two] == False:
        walk(v_two)

sys.setrecursionlimit(1000000)
#print('\n')
#print(sys.getrecursionlimit())


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

# 3. Walk
walk(0)

if n == visitCount:
    print('Yes\n')
else:
    print('No\n')