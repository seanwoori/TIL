# 최소 배터리 사용량을 구하기 위한 dfs 함수
def dfs(n,sm,next):
    '''
    :param n: dfs 재귀 호출을 중단하기 위한 int 자료형 layer 변수
    :param sm: 배터리 사용량을 더하기 위한 int 자료형 sm 변수
    :param next: 시작 강의실을 다음 dfs에 전달하기 위한 int 자료형 next 변수
    :return: 최소 배터리 사용량 ans 값 return
    '''

    global ans

    # 만약 b가 a보다 먼저 도달되었다면, 가지치기
    if v[b] and not v[a]:
        return

    # 만약 sm이 이미 최소값보다 크다면, 가지치기
    if sm>ans:
        return

    # 출발점 0으로 돌아오기 전까지만 고려하기 위해 n==N-1로 종료조건 선언.
    if n==N-1:

        # 이후 sm 변수에 츨발점 0으로 돌아올 때의 배터리 사용량 더해줌.
        sm+=arr[next][0]

        # 만약 ans가 sm보다 크면, ans 갱신
        if sm<=ans:
            ans=sm
        return

    # 출발점으로 돌아오는 경우 제외를 위한 범위 설정 range(1,N)
    # (j,j) 카운팅을 제외시킴.
    for j in range(1,N):
        if not v[j] and next!=j:
            v[j]=1
            dfs(n+1, sm+arr[next][j], j)
            v[j]=0


T = int(input())
for tc in range(1,1+T):
    N = int(input())
    arr=[list(map(int, input().split())) for _ in range(N)]
    a,b=map(int,input().split())

    # 최소 ans를 구하기 위한 초기값 설정
    # visited 배열 설정
    ans=100000
    v=[0]*N

    # dfs 함수 호출
    dfs(0,0,0)

    print(f'#{tc} {ans}')