import sys
sys.stdin = open('input.txt', 'r')

for _ in range(3):
    a = list(map(int, input().split()))
    b = 0
    ans = ''

    for num in a:
        if num == 0:
            b += 1
    if b == 1:
        ans = 'A'
    elif b == 2:
        ans = 'B'
    elif b == 3:
        ans = 'C'
    elif b == 4:
        ans = 'D'
    else:
        ans = 'E'
    print(ans)