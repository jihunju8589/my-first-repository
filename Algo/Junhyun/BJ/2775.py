# https://www.acmicpc.net/problem/2775

apartment = []

for i in range(15):
    line = []
    for j in range(14):
        line.append(0)
    apartment.append(line)

for i in range(0, 14):
    apartment[0][i] = i + 1

for i in range(1, 15):
    for j in range(14):
        apartment[i][j] = apartment[i - 1][j] + apartment[i][j - 1]

test = int(input())
result = []

for i in range(test):
    a = int(input())
    b = int(input())
    result.append(apartment[a][b - 1])

for answer in result:
    print(int(answer))
