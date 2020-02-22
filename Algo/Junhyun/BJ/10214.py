# https://www.acmicpc.net/problem/10214
T=int(input())
x=0
YONSEI=[]
KOREA=[]
y=0
z=0
while(x<9):
    Y, K=input().split()
    Y=int(Y)
    K=int(K)
    YONSEI[y]=Y
    y+=1
    KOREA[z]=K
    z+=1
    x+=1
sum1=0
sum2=0
for i in YONSEI:
    sum1+=i
for t in KOREA:
    sum2+=t
if sum1>sum2:
    print("Yonsei")
elif sum1<sum2:
    print("Korea")
else:
     print("Draw")

