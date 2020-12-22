# answer.py
# 11399 ATM

# ---------------------------

import sys
input = sys.stdin.readline


def main():
    a = [1, 2]

    n = int(input())
    for i in range(n-2):
        a.append(sum(a[-2:]))
    print(a[n-1] % 10007)


main()

