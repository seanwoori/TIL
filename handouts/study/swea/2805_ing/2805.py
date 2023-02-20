import sys
sys.stdin = open('input.txt', 'r')

T=int(input())
for tc in range(1, 1+T):
    N=int(input())
    arr=[list(map(int,input())) for _ in range(N)]
    ans=0
    for i in range(N):
        for j in range(N//2,-(N//2)-1, -1):
            if j==0:
                ans+=sum(arr[i])
            elif j<0:
                j=-j
            temp=sum(arr[i][:j])+sum(arr[i][N-j:])
            ans+=sum(arr[i])-temp
    print(f'#{tc} {ans}')