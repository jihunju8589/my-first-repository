# https://www.acmicpc.net/problem/1193
#2020.02.25.숙제.성공!
Numerator=[]
Denominator=[]
x=int(input())
for i in range(1,x+1):
    if i%2==0:
        for t in range(1,i+1):
            Numerator.append(t)
        for t in range(i,0,-1):
            Denominator.append(t)
    else:
        for t in range(i,0,-1):
            Numerator.append(t)
        for t in range(1,i+1):
            Denominator.append(t)
print(str(Numerator[x-1])+'/'+str(Denominator[x-1]))   