# https://www.acmicpc.net/problem/2863
s1=list(map(int, input().split()))
s2=list(map(int, input().split()))
s3=[]
s3=s1+s2
total=[]
total.append(s3[0]/s3[2]+s3[1]/s3[3])
for i in range(0,4):
    temp=s3[3]
    s3[3]=s3[2]
    s3[2]=s3[1]
    s3[1]=s3[0]
    s3[0]=temp
    total.append(s3[0]/s3[2]+s3[1]/s3[3])
print(max(total))