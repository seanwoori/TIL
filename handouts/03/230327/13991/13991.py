import sys
sys.stdin = open('input.txt', 'r')

def dfs(n, sm):
    global ans
    # 가지치기는 제일 위 ! (최소값을 구해라 == 가지치기를 해라)
    # 더이상 갱신해도 정답 가능성 없을 때 갱신
    if ans<=sm:
        return
    # 종료조건: n에 관련된, 항상 종료될 수 있는 조건으로
    # 종료시점에서 정답처리 !
    if n==N:
        if ans>sm:
            ans=sm
        return
    # n+1 하부함수 호출
    for j in range(0,N):
        if 0<=n<N:
            dfs(n+1, sm+arr[n][j])
            visited[j]=0 # 한번 내려간 이후에는, 다시 돌아올 수 있기 때문에 0으로 clear

    # for j in range(N):
    # if j not in v:
    #     v.append(j)
    #     dfs(n+1, sm+arr[n][j])
    #     v.pop()

    # for j in range(N):
    #     if j not in v:
    #         dfs(n+1, sm+arr[n][j], v+[j])

T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    arr=[list(map(int, input().split())) for _ in range(N)]
    ans = 10*N
    dfs(0, 0)

    print(f'#{tc} {ans}')
