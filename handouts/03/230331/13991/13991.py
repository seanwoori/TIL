import sys
sys.stdin = open('input.txt', 'r')

def dfs(ci,cj,sm):
    global ans

    if sm>ans:
        return

    if (ci,cj)==(N,N):
        ans=min(ans,sm)
        return
    
    if ci<N:
        dfs(ci+1, cj, sm+arr[ci+1][cj])

    if cj<N:
        dfs(ci,cj+1,sm+arr[ci][cj+1])


T=int(input())
for tc in range(1,1+T):
    N=int(input())
    arr = [[0]*(N+1)] + [[0]+list(map(int, input().split()))+[0] for _ in range(N)] + [[0]*(N+1)]
    ans = 1000000

    dfs(1,1,arr[1][1])
    print(f'#{tc} {ans}')