# # https://www.acmicpc.net/problem/8958

# T = int(input())


# def scores(T):
#     x = 0
#     while x < T:
#         s = input()
#         if s[0] == "O":
#             score = 1
#             for i in s:
#                 if i == "O":
#                     if i == :
#                         score += score + 1
#                     elif i != i + 1:
#                         score += 1
#         elif s[0] == "X":
#             score = 0
#             for i in s:
#                 if i == "O":
#                     if i == i + 1:
#                         score += score + 1
#                     elif i != i + 1:
#                         score += 1
#         return score

#     x += 1


# print(scores(T))

s = "OOXXOXXOOO"  # 1 2 0 0 1 0 0 1 2 3
total = int()
score = int()
total
for i in s:
    if i=='X':
        score=0
    if i=='O':
        if i==i-1:
            score+=score+1
            total+=score

