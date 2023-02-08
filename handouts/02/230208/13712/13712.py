import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, 1+T):
    a = list(map(str, input()))

    for idx, char in enumerate(a):
        if char == 'q':
            a[idx] = 'p'
        elif char == 'p':
            a[idx] = 'q'
        elif char == 'b':
            a[idx] = 'd'
        elif char == 'd':
            a[idx] = 'b'

    b = ''.join(a[::-1])
    
    print(f'#{tc} {b}')