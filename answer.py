# answer.py
# 10814 나이순 정렬

from sys import stdin, stdout

n = int(input())
L = []

for i in range(n):
    a, b = stdin.readline().split()
    L.append([int(a), b])

L = sorted(L, key=lambda x: [x[0]])

for i, j in L:
    stdout.write(str(i)+' '+j+'\n')
