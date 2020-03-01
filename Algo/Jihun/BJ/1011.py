# http://acmicpc.net/problem/1011
# 2020.02.25.숙제.실패!

# T = int(input())
# total = []

# for i in range(T):
#     x, y = map(int, input().split())
#     k = 0
#     z = y - x - 1
#     cnt = 0

#     while 1:
#         if k + 1 <= z:
#             z = y - x - 1 - (k + 1)
#             k = k + 1
#         elif k <= z:
#             z = y - x - 1 - k
#         elif k - 1 <= z:
#             z = y - x - 1 - (k - 1)
#             k = k - 1
#         cnt+=1
#         if z<=0:
#             break
#     total.append(cnt + 1)

# for i in total:
#     print(i)


result=[]
T = int(input())
for i in range(T):
    x, y = map(int, input().split())
    num=y-x
    for j in range(num):
        if num==j**2:
            result.append(j+j-1)
        elif j**2<num<=(j**2)+j:
            result.append(j+j)
        elif (j**2)+j<num<(j+1)**2:
            result.append(j+j+1)
for i in result:
    print(i)

