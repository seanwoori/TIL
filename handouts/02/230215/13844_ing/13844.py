import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, 1+T):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]
    visited = [0]*


    print(f'#{tc} {ans}')