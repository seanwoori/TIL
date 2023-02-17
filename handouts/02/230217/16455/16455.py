import sys
sys.stdin = open('input.txt', 'r')

def mulmul(N, M):
    if M==1:
        return N
    else:
        return N*mulmul(N,M-1)

T = 10
for tc in range(1, 1+T):
    _ = int(input())
    N, M = map(int, input().split())
    cnt = 0
    ans = mulmul(N,M)
    print(f'#{tc} {ans}')