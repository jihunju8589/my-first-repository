# http://acmicpc.net/problem/1011
#2020.02.25.숙제.실패!
T=int(input())
total=[]
for i in range(T):
    x, y=map(int, input().split())
    k=0
    z=y-x-1
    cnt=0
    while z>0:
        if k+1<=z:
            z=y-x-1-(k+1)
            k=k+1
        elif k<=z:
            z=y-x-1-k
        elif k-1<=z:
            z=y-x-1-(k-1)
            k=k-1
        cnt+=1
    total.append(cnt+1)
for i in total:
    print(i)