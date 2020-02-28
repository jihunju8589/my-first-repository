# https://www.acmicpc.net/problem/2292
#2020.02.25.숙제.성공!
N=int(input())
t=0
k=0
j=6
cnt=2
if N==1:
    print(1)
else:
    while(1):
        i=2+6*t
        if N>=i and N<i+j:
            print(cnt)
            break
        else:
            j+=6
            cnt+=1
            k+=1
            t+=k

