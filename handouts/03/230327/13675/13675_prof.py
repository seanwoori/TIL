import sys
sys.stdin = open('input.txt', 'r')

def dfs(n, cnt, sm):
    global ans
    # [0] 가지치기는 가장 위에서, 순서로는 가장 마지막에서,
    if cnt>CNT or sm>K:
        return

    # [1] 종료조건 처리(n에 관련) => 정답처리는 이곳에서 !!
    if n==N:
        if cnt==CNT and sm==K:
            ans+=1
        return

    # [2] 하부 호출
    # 사용하는 경우
    dfs(n+1, cnt+1, sm+lst[n])
    # 사용하지 않는 경우
    dfs(n+1, cnt, sm)

T = int(input())
for tc in range(1, 1+T):
    CNT, K = map(int, input().split())
    N=12
    lst=[n for n in range(1, N+1)]

    ans=0
    dfs(0,0,0)
    print(f'#{tc} {ans}')