# https://www.acmicpc.net/problem/2292

room = int(input())

if room == 1:
    print(1)
else:
    num = 1
    answer = 1

    while room >= 2:
        room -= num * 6
        num += 1
        answer += 1

    print(answer)
