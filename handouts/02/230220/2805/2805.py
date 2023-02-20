import sys
sys.stdin = open('input.txt', 'r')

T=int(input())
for tc in range(1, 1+T):
    N=int(input())
    arr=[list(map(int,input())) for _ in range(N)]
    ans=0
    a=list(range(N//2,-(N//2)-1, -1))

    for id,val in enumerate(a):
        if val<0:
            a[id]=-val

    for i in range(N):
        if a[i]==0:
            ans+=sum(arr[i])
            continue
        temp=sum(arr[i][:a[i]])+sum(arr[i][N-a[i]:])
        ans+=sum(arr[i])-temp

    print(f'#{tc} {ans}')