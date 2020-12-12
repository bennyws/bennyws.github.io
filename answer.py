# answer.py
# 1181 단어 정렬

L = []
cL = []

N = int(input())  # 단어의 개수

for i in range(N):  # 단어 입력
    L.append(input())

L.sort()  # 리스트 정렬

for i in range(N):  # 중복 단어 제거
    if L.count(L[i]) > 1:
        for j in range(L.count(L[i]) - 1):
            L.pop(L.index(L[i]))
    if i + 1 >= len(L):  # 리스트 끝에 도달 시 종료
        break

for i in range(len(L)):  # L의 단어 길이를 담은 cL 생성
    cL.append(len(L[i]))

for i in range(len(L), 0, -1):  # 단어 길이순으로 정렬
    n = int(cL.index(min(cL[:i])))
    L.append(L.pop(n))
    cL.append(cL.pop(n))

print(L)
