# https://www.acmicpc.net/problem/5585


money = 1000 - int(input())

coin = 0
while money != 0:
    for num in [500, 100, 50, 10, 5, 1]:
        while money >= num:
            money -= num
            coin += 1

print(coin)
