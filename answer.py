# answer.py
# 2798 블랙잭

n, m = map(int, input().split())  # n : 카드의 개수, m : 기준이 될 수

a = list(map(int, (input().split())))  # 카드를 담을 리스트

maxsum = 0  # 최댓값을 담을 변수

for i in range(0, n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            csum = a[i] + a[j] + a[k]
            if maxsum < csum and csum <= m:
                maxsum = csum

print(maxsum)
