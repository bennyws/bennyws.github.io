# index.py

while True:
    a = input()
    if a == '0': break
    print('Yes' if a == a[::-1] else 'No')
