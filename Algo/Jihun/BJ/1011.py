# http://acmicpc.net/problem/1011
# 2020.02.25.숙제.실패!

T = int(input())
total = []

for i in range(T):
    print("i : {0}".format(i))
    x, y = map(int, input().split())
    print("x : {0}, y : {1}".format(x, y))
    k = 0
    z = y - x - 1
    cnt = 0

    while 1:
        if k + 1 <= z:
            z = y - x - 1 - (k + 1)
            k = k + 1
        elif k <= z:
            z = y - x - 1 - k
        elif k - 1 <= z:
            z = y - x - 1 - (k - 1)
            k = k - 1
        cnt+=1
        if z<=0:
            break
    total.append(cnt + 1)

for i in total:
    print(i)
