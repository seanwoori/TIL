import sys
sys.stdin = open('input.txt', 'r')


# 맵이 조금 커지면 bfs로 풀어야함
def bfs(s):
    # [1] q[], v[] 생성
    q=[]

    # [2] q에 초기데이터(들) 삽입
    # 첫 방문 시 해야할 일 있으면 먼저 진행
    q.append(s)
    visited[s]=1
    alst.append(s)

    while q:
        c=q.pop(0)

        # [3] 4/8방향, 연결된 노드 등 미방문, 조건 맞으면 
        for e in adj[c]:
            if visited[e]==0:
                visited[e]=1
                q.append(e)
                alst.append(e)

    # 가능한 모든 위치 탐색 완료후 필요시 특정값 리턴


def dfs(s):
    # 방문표시: 첫 방문시 처리할 일 있으면 이곳에서..!
    v[s]=1
    alst.append(s)

    for e in adj[s]:
        
        # 연결된 노드이고 미방문시
        if v[e]==0:
            dfs(e)

T = int(input())
for tc in range(1,1+T):
    V,E = map(int,input().split())
    
    adj=[[] for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int, input().split())
        adj[s].append(e)    
        adj[e].append(s)    # 양방향 연결이므로...

    # 여러개 연결시 낮은 번호부터 방문! => 오름차순 정렬
    for lst in adj:
        lst.sort()

    visited=[0]*(V+1)
    v=[0]*(V+1)
    alst=[]
    bfs(1)

    print(f'#{tc}', *alst)
