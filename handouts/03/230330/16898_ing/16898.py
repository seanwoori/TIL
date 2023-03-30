import sys
sys.stdin = open('input.txt', 'r')

def dfs(n,sm,idx):
    global ans
    if sm>K:
        return

    if n>=N:
        return

    if sm==K:
        ans+=1
        return

    for i in range(idx,N):
        if not v[i]:
            v[i]=1
            dfs(n+1,sm+lst[i],idx+1)
            v[i]=0

T = int(input())
for tc in range(1, 1+T):
    N,K = map(int,input().split())
    lst = list(map(int, input().split()))
    v=[0]*N

    ans=0
    dfs(0,0,0)

    print(f'#{tc} {ans}')