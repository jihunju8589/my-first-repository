# https://www.acmicpc.net/problem/1789

s = int(input())
n = 1

while n * (n + 1) / 2 <= s:
    n += 1

print(n - 1)
