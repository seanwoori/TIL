import sys
sys.stdin = open('input.txt', 'r')

def dfs(n,sm,s):
    global ans
    if sm>ans:
        return

    # n은 단지 종료조건을 위한 수
    if n==N:
        ans=min(sm+arr[s][1],ans)
        return

    # s는 안돌아도 되는 변수, 따라서 다음 레이어로 전달만 가능하면 된다.
    for j in range(2,N+1):
        if not visited[j]:
            visited[j]=1
            dfs(n+1,sm+arr[s][j], j)
            visited[j]=0

T = int(input())
for tc in range(1, 1+T):
    N=int(input())
    arr =[[0]*(N+1)] + [[0]+list(map(int, input().split()))+[0] for _ in range(N)] + [[0]*(N+1)]
    ans = 1000000
    visited=[0]*(N+1)

    # 방문구역수, 사용량, 시작구역번호
    dfs(1,0,1)

    print(f'#{tc} {ans}')
