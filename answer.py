# answer.py
# 1764 듣보잡

# ---------------------------

import time
import sys
input = sys.stdin.readline

start = time.time()


def main():
    n, m = map(int, input().split())
    a = set()
    b = set()

    for i in range(n):
        a.add(input().strip())

    for i in range(m):
        b.add(input().strip())

    L = a & b

    print(len(L), sorted(L))
    for i in sorted(L):
        print(i)


main()

# ---------------------------
print("time :", time.time() - start)
