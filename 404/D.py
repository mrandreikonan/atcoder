
import sys

n = 0
m = 0
cost = []
a = []
z = []
min_cost = sys.maxsize

def getInput(file):
    global cost
    global n
    global m
    global a
    global z
    global min_cost

    lines = []

    if True == file:
        file = open('D_input1.txt', 'r')
        text = file.read()
        lines=text.split('\n')
        file.close()
        n, m = map(int, lines[0].split())
    else:
        size_line = input()
        n, m = map(int, size_line.split())
        lines.append([])
        lines.append(input()) # cost
        for i in range(0,m):
            lines.append(input()) # animal map
    
    cost = [0] + list(map(int, lines[1].split()))

    a.append([])
    z = [[] for i in range(0,n+1)]


    for k in range(1, m + 1):
        animal = list(map(int,lines[k+1].split()))
        animal.pop(0)
        a.append(animal)
    
    # Construct zoo vs animal map
    for animal in range(1, len(a)):
        for zoo in a[animal]:
            z[zoo].append(animal)

    min_cost = 2 * sum(cost)

def calculate_total_cost(zoos):
    global cost
    global n
    sum = 0
    for i in range(1,n+1):
        sum += zoos[i] * cost[i]
    return sum

def all_animals_seen_twice(animal_seen):
    for animal in animal_seen[1:len(animal_seen)]:
        if animal < 2:
            return False
        
    return True

def zoo(zoos, position, animals_seen):
    global n
    global z
    global min_cost

    # Calculate cost
    visit_cost = calculate_total_cost(zoos)

    # if pending cost is already about best found - stop
    if visit_cost > min_cost:
        return

    if (visit_cost > 0) and (visit_cost < min_cost) and (True == all_animals_seen_twice(animals_seen)):
        min_cost = visit_cost
        return

    if position == n+1:
        return
    
    # 0 visit
    zoo(zoos[:], position+1, animals_seen[:])

    # 1 visit
    zoos[position] = 1
    for animal in z[position]:
        animals_seen[animal] += 1
    zoo(zoos[:], position+1, animals_seen[:])

    # 2 visit
    zoos[position] = 2
    for animal in z[position]:
        animals_seen[animal] += 1
    zoo(zoos[:], position+1, animals_seen[:])

getInput(False)

zoos = [0 for i in range(0,n+1)]
#zoos[1] = 1

animals_seen = [0 for i in range(0,m+1)]
#for animal in z[1]:
#    animals_seen[animal] += 1
zoo(zoos, 1, animals_seen)
print(min_cost)