def length(a, b):
    c=a*a+b*b
    for i in range(1,c):
        if(c/i==i):
            return i
            break
a=8
b=6
i=length(a,b)
print(i)
#대각선 길이 구하기