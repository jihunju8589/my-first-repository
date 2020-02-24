# https://www.acmicpc.net/problem/4101
# s=[]
# x=0
# while(1):    
#     s[x], s[x+1]=map(int, input().split())
#     if s[x]==s[x+1]==0:
#         break
#     x+=2
# print(s[3])
#아몰랑!
while(1):
    a, b=map(int, input().split())
    if a==b==0:
        break
if a>b:
    print("Yes")
elif a==b==0:
    print(" ")
else print("No")

    
