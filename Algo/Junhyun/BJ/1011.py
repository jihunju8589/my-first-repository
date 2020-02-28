# http://acmicpc.net/problem/1011

# case_num = int(input())
# ans = []
# for i in range(case_num):
#     a, b = map(int, input().split())
#     num = b - a
#     k = 1
#     p = 1
#     while num > 0:
#         num -= k
#         k += 1
#         if num >= p:
#             num -= p
#             p += 1

#     ans.append(k + p - 2)

# for i in ans:
#     print(i)

t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    c = b - a
    num = 1
    while True:
        if num ** 2 <= c < (num + 1) ** 2:
            break
        num += 1
    if num ** 2 == c:
        print((num * 2) - 1)
    elif num ** 2 < c <= num ** 2 + num:
        print(num * 2)
    else:
        print((num * 2) + 1)
