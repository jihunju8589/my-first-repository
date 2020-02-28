# https://www.acmicpc.net/problem/2775
#2020.02.25.숙제.모름.

appartment=[]
for i in range(15):
    line=[]
    for j in range(14):
        line.append(0)
    appartment.append(line)

for j in range(0,14):
    appartment[0][j]=j+1

for i in range(1,15):
    for j in range(0,14):
        appartment[i][j]=appartment[i-1][j]+appartment[i][j-1]

T=int(input())
answer=[]

for i in range(T):
    k=int(input())
    n=int(input())
    answer.append(appartment[k][n-1])
    
for i in answer:
    print(int(i))
###############################
