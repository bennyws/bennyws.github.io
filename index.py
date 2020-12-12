# index.py

col, row = map(int, input().split())

matrix = []
for i in range(row):
    matrix.append(list(input()))

for i in range(col):
    for j in range(row):
        if matrix[i][j] == '.':
            count = 0
            for m in range(i-1, i+2):
                if m < 0 or m >= col:
                    continue
                for n in range(j-1, j+2):
                    if n < 0 or n >= row:
                        continue
                    if matrix[m][n] == '*':
                        count += 1
            matrix[i].pop(j)
            matrix[i].insert(j, count)

for i in range(col):
    for j in matrix[i]:
        print(j, end="")
    print()
