# https://www.acmicpc.net/problem/10039
#성공!
s=[]
for i in range(0,5):
    a=int(input())
    if a>=40:
        s.append(a)
    else:
        s.append(40)
print(sum(s)/5)
