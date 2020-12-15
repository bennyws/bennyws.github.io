# answer.py
# 10866 덱

# ---------------------------

import time
import sys
input = sys.stdin.readline

start = time.time()

N, K = map(int, input().split())
start = time.time()
a = list(i+1 for i in range(N))

count = 0
print('<', end='')
while len(a) > 0:
    count -= 1
    count += K
    while count >= len(a):
        count -= len(a)
    print(a.pop(count), end='')
    if len(a) > 0:
        print(', ', end='')
    else:
        print('>')

# ---------------------------
print("time :", time.time() - start)
