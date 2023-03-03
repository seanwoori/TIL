import sys
sys.stdin = open('input.txt', 'r')

T=int(input())
for tc in range(1,1+T):
    N,K=map(int, input().split())
    lst=list(map(int, input().split()))
    lst.sort(reverse=True)
    ans=0
    for i in range(K):
        ans+=lst[i]

    print(f'#{tc} {ans}')