# https://www.acmicpc.net/problem/1789
S=int(input())
for i in range(1, S):
    a+=i
    if a==S:
        print i
        break
    else:
        def same(S):
            for i in range(1,S):
                for x in range(1,S):
                    b+=i+x
                    if b==S:
                        print i
                        break
                    else:
                        same(S)

s=int(input())
n=1
while n*n(n+1)/2<=s:
    n+=1
print(n-1)        