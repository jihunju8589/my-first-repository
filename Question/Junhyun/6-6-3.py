# # # 숫자, 문자열 구별하기


# # def set(string):
# #     arr1 = []
# #     arr2 = []
# #     # t = 0
# #     # x = 0

# #     # append : 리스트 원소 마지막에 추가
# #     # insert : 리스트.index(입력할 index, 값)

# #     for i in string:
# #         if i >= "A" and i <= "z":
# #             arr1.append(i)
# #         else:
# #             arr2.append(i)

# #     print("str:", end="")  # print 함수 인자 end에 원하는 문자를 넣어주면 줄바꿈 대신 원하는 문자가 추가되어 출력됨

# #     for y in arr1:
# #         print(y, end="")

# #     print("\n")

# #     print("int:", end="")

# #     for w in arr2:
# #         print(w, end="")


# # string = input()  # str이 전달됨

# # set(string)


a = input()
s = str()
n = str()

for i in a:

    print("Now number : {0}".format(i))

    try:
        print("Try Status : {0}".format(i))
        int(i)
        n += i
        print("Try Complete : {0}".format(i))

    except:
        print("Except Status : {0}".format(i))
        s += i
        print("Except Complete : {0}".format(i))

print(s, n)
