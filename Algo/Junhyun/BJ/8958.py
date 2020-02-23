# https://www.acmicpc.net/problem/8958


N = int(input())

for i in range(N):
    O_Score = 0
    Total_Score = 0
    A = input()

    for B in A:
        if B == "O":
            O_Score += 1
            Total_Score += O_Score
        else:
            O_Score = 0

    print(Total_Score)
