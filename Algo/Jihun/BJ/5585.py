# https://www.acmicpc.net/problem/5585
T=int(input())
change=1000-T
if change>500:
    a=(change-500)//100
    b=(change-500-100*a)//50
    c=(change-500-100*a-50*b)//10
    d=(change-500-100*a-50*b-10*c)//5
    e=(change-500-100*a-50*b-10*c-5*d)//1
    cnt=1+a+b+c+d+e
elif 100<change<500:
    a=change//100
    b=(change-100*a)//50
    c=(change-100*a-50*b)//10
    d=(change-100*a-10*b-10*c)//5
    e=(change-100*a-10*b-5*c-5*d)//1
    cnt=a+b+c+d+e
elif 50<change<100:
    a=change//50
    b=(change-50*a)//10
    c=(change-50*a-10*b)//5
    d=(change-50*a-10*b-5*c)//1
    cnt=a+b+c+d
elif 10<change<50:
    a=change//10
    b=(change-10*a)//5
    c=(change-10*a-5*b)//1
    cnt=a+b+c
elif 5<change<10:
    a=change//5
    b=(change-5*a)//1
    cnt=a+b
else:
    cnt=change//1
print(cnt)