# while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.

result = 0
count = 1

while count <= 1000:
    if count % 3 == 0: # 3으로 나누어 떨어지는 수는 3의 배수
        result += count
    
    count += 1 

print(result) # 166833 출력