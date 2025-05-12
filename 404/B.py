def rotate(matrix, size):
    result = []
    for col in range(0, size):
        line = ''
        for row in range(size-1, -1, -1):
            line += matrix[row][col]
        result.append(line)
    return result

def compare(matrixA, matrixB, size):
    diffCount = 0;
    for row in range(0, size):
        for col in range(0, size):
            if matrixA[row][col] != matrixB[row][col]:
                diffCount += 1
    return diffCount

#file = open('B_input3.txt', 'r')
#text = file.read()
#lines=text.split('\n')
#file.close()
#n = int(lines[0])
#s = lines[1:n+1]
#t = lines[n+1:len(lines)]

n = int(input())
s = []
for lineIdx in range(0,n):
    s.append(input())
t = []
for lineIdx in range(0,n):
    t.append(input())

s90 = rotate(s, n)
s180 = rotate(s90, n)
s270 = rotate(s180, n)

compares = [compare(s, t, n), compare(s90, t, n), compare(s180, t, n), compare(s270, t, n)]

answer = 1000000

for rotation in range(0,4):
    if (compares[rotation] + rotation) < answer:
        answer = compares[rotation] + rotation

print(answer)