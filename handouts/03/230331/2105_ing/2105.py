import sys
sys.stdin = open('input.txt', 'r')

dr = [
    (1,1),
    (1,-1),
    (-1,-1),
    (-1,1)
    ]

def desert(n,ci,cj,cnt):
    global ans

    if n:
        if (ci,cj)==(ti,tj):
            return

    for di,dj in dr:
        ni,nj=ci+di, cj+dj
        if 0<=ni<N and 0<=nj<N and (ni,nj) not in v and arr[ni][nj] not in v:
            v.append(arr[ni][nj])
            v.append((ni,nj))
            desert(n+1,ni,nj,cnt+1)
            v.pop()
            v.pop()


T=int(input())
for tc in range(1,1+T):
    N=int(input())
    arr=[list(map(int, input().split())) for _ in range(N)]

    ans=0
    for ti in range(N):
        for tj in range(N):
            v=[]
            desert(0,ti,tj,1)

    print(f'#{tc} {ans}')

