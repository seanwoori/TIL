import sys
sys.stdin = open('input.txt', 'r')

'''
교수님 풀이
행을 지나가면서 확인한 행을 지우면 된다.
n==N break
배열의 인덱스는 행의 번호로 잡으면 풀이가 쉬울 것임.
일반화를 시켜줘야함.
처음 선택은 N-1까지 가능함.
다음 인덱스에서도 N-1까지의 선택이 가능한가?
visited 배열을 이용하여 방문한 배열을 제외시킬 수 있음.
종료조건에서는 여태까지의 합을 구해야함.
dfs 함수는 박스 하나를 짜는 것임.
'''

def dfs(n, sm):
    global ans
    # 가지치기는 제일 위 ! (최소값을 구해라 ! = 가지치기를 해라)
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
        if not visited[j]:
            visited[j]=1 # visited 배열 1로 체킹
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
    visited=[0]*N
    ans = 10*N
    dfs(0, 0)

    print(f'#{tc} {ans}')