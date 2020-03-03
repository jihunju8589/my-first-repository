# https://www.acmicpc.net/problem/6603


from itertools import combinations  # 조합을 사용하여 해결

number_list = list(map(int, input().split()))

while number_list != [0]:  # 인풋이 0이면 while문 탈출
    number_list = sorted(number_list[1:])  # 순서대로 나오게 정렬 먼저

    for numbers in list(combinations(number_list, 6)):  # 조합 함수를 사용
        for num in numbers:
            print(num, end=" ")
        print()
    print()

    number_list = list(map(int, input().split()))
