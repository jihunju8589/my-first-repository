# https://www.acmicpc.net/problem/11653
# 개어려워

N = int(input())
x = 0
prime = [2]

for i in range(3, N):
    for t in range(2, i):
        if i % t == 0:
            break
        else:
            x += 1
    if x == N - 2:
        prime.append(i)  # 배열에 값이 안들어감

for a in prime:
    if N % a == 0:
        print(a)

# 소수 판단
# for t in range(2,N):
#     if N%t==0:
#         break
#     x+=1
# if(x==N-2):
#     prime.append(N)
# print(prime[1])
