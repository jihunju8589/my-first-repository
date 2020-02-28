# https://www.acmicpc.net/problem/2941
#2020.02.25.숙제.실패! 왜 안되지?!
a=input()
t=len(a)
cnt=0
x=0
i=0
s=[]
for i in range(t):
    s.append(a[i])
while i<t:
    if s[i]=='c' and s[i+1]=='=':
        cnt+=1
        i+=2
    elif s[i]=='c' and s[i+1]=='-':
        cnt+=1
        i+=2
    elif s[i]=='d' and s[i+1]=='z' and s[i+2]=='=':
        cnt+=1
        i+=3
    elif s[i]=='d' and s[i+1]=='-':
        cnt+=1
        i+=2
    elif s[i]=='l' and s[i+1]=='j':
        cnt+=1
        i+=2
    elif s[i]=='n' and s[i+1]=='j':
        cnt+=1
        i+=2
    elif s[i]=='s' and s[i+1]=='=':
        cnt+=1
        i+=2
    elif s[i]=='z' and s[i+1]=='=':
        cnt+=1
        i+=2
    else:
        i+=1
        cnt+=1
print(cnt)

