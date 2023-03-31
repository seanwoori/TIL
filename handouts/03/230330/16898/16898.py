import sys
sys.stdin = open('input.txt', 'r')
def dfs(n,sm):
    global ans

    if sm>K:
        return

    if sm==K:
        ans+=1
        return

    if n==N:
        return

    dfs(n+1, sm+lst[n])
    dfs(n+1, sm)


T = int(input())
for tc in range(1, 1+T):
    N,K=map(int, input().split())
    lst = list(map(int, input().split()))
    ans = 0


    dfs(0,0)
    print(f'#{tc} {ans}')