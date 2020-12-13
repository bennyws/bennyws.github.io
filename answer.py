# answer.py
# 1920 수 찾기


def Binary_Search(L, N):
    a = len(L)//2
    if N > L[a]:
        if(len(L) == 1):
            return False
        L = L[a+1:]
        return Binary_Search(L, N)
    elif N < L[a]:
        if(len(L) == 1):
            return False
        L = L[:a]
        return Binary_Search(L, N)
    else:
        return True


a = [17, 28, 43, 67, 88, 92, 100]
print(Binary_Search(a, 67))



"""import sys
input = sys.stdin.readline

input()
A = set(map(int, input().split()))
input()
B = list(map(int, input().split()))

for i in B:
    if i in A:
        sys.stdout.write('1\n')
    else:
        sys.stdout.write('0\n')"""
