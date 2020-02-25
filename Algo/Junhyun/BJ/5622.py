# https://www.acmicpc.net/problem/5622

A, B, C = 3, 3, 3
D, E, F = 4, 4, 4
G, H, I = 5, 5, 5
J, K, L = 6, 6, 6
M, N, O = 7, 7, 7
P, Q, R, S = 8, 8, 8, 8
T, U, V = 9, 9, 9
W, X, Y, Z = 10, 10, 10, 10

word = input()
word_number = []
for i in range(len(word)):
    word_number.append(eval(word[i]))
print(sum(word_number))
