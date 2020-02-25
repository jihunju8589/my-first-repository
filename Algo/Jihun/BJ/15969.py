# https://www.acmicpc.net/problem/15969
#성공!
N=int(input())
s=list(map(int, input().split()))
s.sort()
print(s[N-1]-s[0])
