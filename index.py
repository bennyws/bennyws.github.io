h = int(input())

for i in range(h):
    for j in range(h * 2 - 1):
        if j < h - i - 1:
            print(' ', end='')
        elif j >= h + i:
            print(' ', end='')
        else:
            print('*', end='')
    print()

