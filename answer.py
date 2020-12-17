# answer.py
# 1003 피보나치 함수

# ---------------------------

import sys
input = sys.stdin.readline


zero = 0
one = 0


def fibonacci(n):
    global zero
    global one
    if n == 0:
        zero += 1
        return
    elif n == 1:
        one += 1
        return
    elif n == 2:
        zero += 2
        one += 1
    else:
        fibonacci(n-1)
        fibonacci(n-2)
        return


def main():
    n = int(input())
    global zero
    global one
    for i in range(n):
        zero = 0
        one = 0
        fibonacci(int(input()))
        print(zero, one)


main()
