# answer.py
# 1764 듣보잡

# ---------------------------

import sys
input = sys.stdin.readline


class Number():
    def __init__(self):
        self.zero = 0
        self.one = 0

    def fibonacci(self, n):
        if n == 0:
            self.zero += 1
            return 0
        elif n == 1:
            self.one += 1
            return 1
        else:
            return self.fibonacci(n-1) + self.fibonacci(n-2)

    def print_num(self):
        print(self.zero, self.one)


def main():
    n = int(input())

    for i in range(n):
        num = Number()
        num.fibonacci(int(input()))
        num.print_num()


main()
