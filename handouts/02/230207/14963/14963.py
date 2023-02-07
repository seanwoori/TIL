import sys
sys.stdin = open('input.txt', 'r')

def bs(lst, s, e, d):
    while s<=e:
        m=(s+e)//2
        if lst[m]==d:
            return m+1
        elif d<lst[m]:
            e=m-1
        else:
            s=m+1
    return 0

T = int(input())
for tc in range(1, T+1):
    N, D = map(int, input().split())
    lst = list(map(int, input().split()))

    ans = bs(lst, 0, N, D)
    print(f'#{tc} {ans}')