# https://www.acmicpc.net/problem/10162
T=int(input())
def count(T):
    A=300
    B=60
    C=10
    x=0
    y=0
    z=0
    q=0
    for i in range(1,33):
        if T-A*i < 0:
            x=i-1
            i=0
            if (T-A*x-B*i)<0:
                y=i-1
                i=0
                if T-A*x-B*y-C*i==0:
                    z=i
                else: q=-1
            if T-A*x-B*i==0:
                y=i
        if T-A*i==0:
            x=i
    
    if q!=0:
        print(x, y, z)
    else: print(q)

print(count())