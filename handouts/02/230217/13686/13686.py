import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, 1+T):
    n = int(input())
    lst = list(map(int, input().split()))
    sm = 0
    mx = 1
    for num in lst[::-1]:
        if mx>num:
            sm += mx-num
        else:
            mx=num

    print(f'#{tc} {sm}')