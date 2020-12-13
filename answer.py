# answer.py
# 2751 수 정렬하기 2

from sys import stdin, stdout

n = int(input())
l = []

for i in range(n):
    l.append(int(stdin.readline()))

for i in sorted(l):
    stdout.write(str(i)+'\n')
