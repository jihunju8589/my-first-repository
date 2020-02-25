# https://www.acmicpc.net/problem/4949
x1=x2=0
y1=y2=0
t=[]
while(1):
    s=input()
    for i in s:
        if i=="(":
            x1+=1
        if i==")":
            x2+=1
        if i=="[":
            y1+=1
        if i=="]":
            y2+=1
    if x1==x2 and y1==y2:
        t.append(0)
    else:
        t.append(1)
    if(s=="."):
        break
for i in t:
    if i==0:
        print("yes")
    else:
        print("no")