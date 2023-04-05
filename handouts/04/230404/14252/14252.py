INF = 50*10

def dijkstra(s, e):
    # [0] D table, v[] 생성 및 시작위치 방문표시
    D = adj[s][::]
    v=[0]*N
    v[s]=1

    # N-1개 노드에 대해서 반복처리
    for _ in range(N-1):
        # [1] 미방문 노드중 기준노드(최소비용으로 연결 가능한)
        mn, i_min = INF,0
        for j in range(N):
            if v[j]==0 and mn>D[j]:
                mn, i_min = D[j], j
        v[i_min] = 1

        # [2] 모든 노드에 대해서 최소비용 갱신(D[])
        for j in range(N):
            # 현재 j까지 가는 비용, 기준노드를 경유해서 가는 비용
            D[j] = min(D[j], D[i_min]+adj[i_min][j])

    return D[e]

T = int(input())

for tc in range(1,1+T):
    N,E = map(int,input().split())
    
    adj=[[INF]*N for _ in range(N)]
    
    for i in range(N):
        adj[i][i]=0
    
    for _ in range(E):
        s,e,w=map(int, input().split())
        adj[s][e]=w
    
    ans=dijkstra(0, N-1)
    print(f'#{tc} {ans}')