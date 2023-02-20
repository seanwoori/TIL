import sys
sys.stdin = open('input.txt', 'r')

T=int(input())
for tc in range(1, 1+T):
    N,M=map(int, input().split())
    lst=list(map(int, input().split()))

    for _ in range(M):
        lst.append(lst.pop(0))
    ans = lst[0]
    print(f'#{tc} {ans}')