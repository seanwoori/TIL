import sys
sys.stdin = open('input.txt', 'r')

def dfs(ci,cj,n,st):
    global ans

    if n==7:
        if st not in temp:
            ans+=1
            temp.append(st)
        return

    if 0<=ci+1<N:
        dfs(ci+1,cj,n+1,st+arr[ci+1][cj])

    if 0<=ci-1<N:
        dfs(ci-1,cj,n+1,st+arr[ci-1][cj])

    if 0<=cj+1<N:
        dfs(ci,cj+1,n+1,st+arr[ci][cj+1])

    if 0<=cj-1<N:
        dfs(ci,cj-1,n+1,st+arr[ci][cj-1])


T = int(input())
for tc in range(1,1+T):
    arr = [list(map(str, input().split())) for _ in range(4)]
    N=4
    ans=0
    temp = []

    for ci in range(N):
        for cj in range(N):
            dfs(ci, cj, 1, arr[ci][cj])

    print(f'#{tc} {ans}')