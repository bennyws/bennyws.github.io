# answer.py
# 정렬 연습 - 2750 수 정렬하기

# ---------------------------

import sys
input = sys.stdin.readline

n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))

array.sort()

for i in range(n):
    print(array[i])
