# https://www.acmicpc.net/problem/11728

import sys

read = lambda: sys.stdin.readline().strip()
sys.setrecursionlimit(10 ** 6)

n, m = map(int, read().split())
a = list(map(int, read().split()))
b = list(map(int, read().split()))

c = [0] * (n + m + 1)

i = j = k = 0
while i < n or j < m:
    k += 1
    if j >= m or (i < n and a[i] <= b[j]):
        c[k] = a[i]
        i += 1
    else:
        c[k] = b[j]
        j += 1

for i in range(1, len(c)):
    print(c[i], end=" ")

