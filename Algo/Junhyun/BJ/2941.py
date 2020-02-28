# https://www.acmicpc.net/problem/2941

# 박준현

# croatian_word = str(input())
# croatian_reference = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
# for word in croatian_reference:
#     print("word : {0}".format(word))
#     croatian_word = croatian_word.replace(word, "0")

# print(croatian_word)
# print(len(croatian_word))

# 주지훈 코드 첨삭

a = input()
cnt = 0
s = []

for i in range(len(a)):
    s.append(a[i])

i = 0

while i < len(a):
    if s[i] == "c" and s[i + 1] == "=":
        cnt += 1
        i += 2
    elif s[i] == "c" and s[i + 1] == "-":
        cnt += 1
        i += 2
    elif s[i] == "d" and s[i + 1] == "z" and s[i + 2] == "=":
        cnt += 1
        i += 3
    elif s[i] == "d" and s[i + 1] == "-":
        cnt += 1
        i += 2
    elif s[i] == "l" and s[i + 1] == "j":
        cnt += 1
        i += 2
    elif s[i] == "n" and s[i + 1] == "j":
        cnt += 1
        i += 2
    elif s[i] == "s" and s[i + 1] == "=":
        cnt += 1
        i += 2
    elif s[i] == "z" and s[i + 1] == "=":
        cnt += 1
        i += 2
    else:
        i += 1
        cnt += 1

print(cnt)

