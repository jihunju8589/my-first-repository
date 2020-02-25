# https://www.acmicpc.net/problem/15969

N = int(input())
N_list = list(map(int, input().split()))
print(max(N_list) - min(N_list))

