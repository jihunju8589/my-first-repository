# https://www.acmicpc.net/problem/5585

#방법1
money = 1000 - int(input())

coin = 0
while money != 0:
    for num in [500, 100, 50, 10, 5, 1]:
        while money >= num:
            money -= num
            coin += 1

print(coin)
#########################
#방법2(내가 함)
money = 1000 - int(input())
num=0
line=[500, 100, 50, 10, 5, 1]
while money!=0:
    for change in line:
        num+=money//change
        money%=change
print(num)
