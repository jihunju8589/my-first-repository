# 다음은 두 개의 숫자를 입력받아 더하여 돌려주는 프로그램이다.

# input1 = input("첫번째 숫자를 입력하세요:")
# input2 = input("두번째 숫자를 입력하세요:")

# total = input1 + input2
# print("두 수의 합은 %s 입니다" % total)


# 이 프로그램을 수행해 보자.

# 첫번째 숫자를 입력하세요:3
# 두번째 숫자를 입력하세요:6
# 두 수의 합은 36 입니다


# 3과 6을 입력했을 때 9가 아닌 36이라는 결괏값을 돌려주었다. 이 프로그램의 오류를 수정해 보자.

# ※ int 함수를 사용해 보자.

input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")

input1 = int(input1)
input2 = int(input2)

total = input1 + input2
print("두 수의 합은 %s 입니다" % total)