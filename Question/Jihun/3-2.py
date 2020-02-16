# while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.
a=3
sum=0
while a<1000:
    sum+=a
    a+=3
print(sum)