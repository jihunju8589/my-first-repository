# https://www.acmicpc.net/problem/10214
#나도 맞음
# T=int(input())
# x=0
# YONSEI=[]
# KOREA=[]
# y=0
# z=0
# while(x<9*T):
#     Y, K=input().split()
#     Y=int(Y)
#     K=int(K)
#     YONSEI.append(Y)
#     y+=1
#     KOREA.append(K)
#     z+=1
#     x+=1
# sum1=0
# sum2=0
# for i in YONSEI:
#     sum1+=i
# for t in KOREA:
#     sum2+=t
# if sum1>sum2:
#     print("Yonsei")
# elif sum1<sum2:
#     print("Korea")
# else:
#      print("Draw")

T=int(input())
for i in range(T):
    y=k=0
    for i in range(9):
        Y, K=map(int, input().split())
        y+=Y
        k+=K
if y>k:
    print("Yonsei")
elif y<k:
    print("Korea")
else:
     print("Draw")

