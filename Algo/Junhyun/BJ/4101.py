# https://www.acmicpc.net/problem/4101

s = []
x = 0

while 1:
    a, b = map(int, input().split())
    s.append(a)
    s.append(b)
    x += 1

    if a == b == 0:
        break

for i in range(0, x, 2):
    if s[i] > s[i + 1]:
        print("Yes")
    elif s[i] == s[i + 1] == 0:
        break
    else:
        print("No")
