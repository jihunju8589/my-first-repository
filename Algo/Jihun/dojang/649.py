def multiple(x, n):
    cnt=0
    for i in range(1, x):
        if(n*i==x):
            print("{0}는 {1}의 배수이다". format(x,n))
            break
        else: cnt+=1
    if(cnt==x-1): print("배수가 아니다")
#n의 배수 판정법
#배수가 아니다가 출력되지 않는 이유를 모르겠어요ㅠ
#x는 n의 배수이다 라고 출력하고 싶은데 그건 어떻게 하죠?!
i=multiple(9,2)

i=multiple(4,2)
