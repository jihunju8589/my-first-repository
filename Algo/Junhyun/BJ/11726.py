# https://www.acmicpc.net/problem/11726


def squares(n):
    answer = 0
    temp_n1 = 1
    temp_n2 = 2

    for i in range(1, n + 1):
        if i == 1:
            answer += 1
        elif i == 2:
            answer += 1
        else:
            answer = temp_n1 + temp_n2
            temp_n1 = temp_n2
            temp_n2 = answer
    return answer


answer = squares(int(input()))
print(answer % 10007)
