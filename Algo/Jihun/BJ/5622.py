# https://www.acmicpc.net/problem/5622
#2020.02.25.숙제.성공!
a=str(input())
s=[]
for i in a:
    s.append(ord(i))
sum=0
for i in s:
    k=3
    t=ord('A')
    while(1):
        if i>=t and i<t+3:
            sum+=k
            break
        t+=3
        k+=1
print(sum)