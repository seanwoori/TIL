import sys
sys.stdin = open('input.txt', 'r')

def dfs(n, cnt, sm):
    global ans
    if ans<=cnt:
        return

    if n==N:
        ans=min(cnt,ans)
        return

    if sm>0:
        dfs(n+1, cnt, sm-1)

    dfs(n+1, cnt+1, lst[n]-1)

T = int(input())
for tc in range(1,1+T):
    lst=list(map(int,input().split()))
    N=lst[0]
    ans=N
    dfs(2, 0, lst[1]-1)

    print(f'#{tc} {ans}')