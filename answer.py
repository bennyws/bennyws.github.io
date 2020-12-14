# answer.py
# 10816 숫자 카드 2


import time
start = time.time()

import sys
from collections import Counter
input = sys.stdin.readline


_ = input()
a = input().split()
_ = input()
b = input().split()


c = Counter(a)
print(' '.join(f'{c[m]}' if m in c else '0' for m in b))

print("time :", time.time() - start)
