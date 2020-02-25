# https://www.acmicpc.net/problem/2941

croatian_word = str(input())
croatian_reference = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
for word in croatian_reference:
    croatian_word = croatian_word.replace(word, "0")
print(len(croatian_word))
