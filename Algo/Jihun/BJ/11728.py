# https://www.acmicpc.net/problem/11728
#성공!
N, M=input().split()
n=list(map(int, input().split()))
m=list(map(int, input().split()))
s=[]
s=n+m
s.sort()
print(s)

