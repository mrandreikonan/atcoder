"""file = open('C_input1.txt', 'r')
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

def walk(start):
    visit[start] = True
    neighbours = v[start][:]

    # remove all the edges with neighbours
    start_neigh = v[start][:]
    for neigh in start_neigh:
        v[neigh].remove(start)
        v[start].remove(neigh)

    while (len(neighbours) > 0):
        current = neighbours[0];

        if visit[current] == True:
            return False
        else:
            visit[current] = True

        current_neigh = v[current][:]
        for i in current_neigh:
            if i in neighbours:
                return False
            else:
                neighbours.append(i)
                v[i].remove(current)
                v[current].remove(i)

        neighbours.pop(0)

    return True

answer = 'No\n'

while visitCount < n:
    start = 0
    # Select next non visited
    for i in range(0,n):
        if (visit[i] == False):
            start = i
            break
    
    if False == walk(start):
        break;
print(answer)