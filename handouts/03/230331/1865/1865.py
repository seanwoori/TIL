import sys
sys.stdin = open('input.txt', 'r')

def dongchul(n,sm):
    global ans

    # 확률이 0일 경우 가지치기
    if not sm:
        return

    # 확률이 이미 작을 경우 가지치기
    if sm<=ans:
        return

    if n==N:
        ans=max(ans,sm)
        return

    for j in range(N):
        if not v[j]:
            v[j]=1
            dongchul(n+1,sm*arr[n][j])
            v[j]=0


T = int(input())
for tc in range(1,1+T):
    N=int(input())
    arr=[list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr[i][j]=arr[i][j]/100
    v=[0]*N

    ans=0
    dongchul(0,1)
    print(f'#{tc} {ans*100:0.6f}')
