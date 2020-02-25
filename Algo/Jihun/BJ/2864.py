# https://www.acmicpc.net/problem/2864
A, B=input().split()
replaceAll1=int(A.replace("5", "6"))
replaceAll2=int(B.replace("5", "6"))
replaceAll3=int(A.replace("6", "5"))
replaceAll4=int(B.replace("6", "5"))
print(replaceAll3+replaceAll4, replaceAll1+replaceAll2)