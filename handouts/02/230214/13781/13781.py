import sys
sys.stdin = open('input.txt', 'r')

# 인접리스트 방법
# 그래프가 정렬되어 있다는 보장이 없음.
# 따라서 오름차순으로 정렬해야함.
# 이후 하나씩 pop.


# 인접행렬 방법
def dfs_stk(adj, start):
    vst = [0]*(v+1)
    stk = []

    s = start
    vst[s]=1
    alst.append(s)

    while True:
        # s 에서 연결된 미방문 노드 발견시 이동.
        # 다만, 낮은 번호에서 높은 번호로.
        for e in range(1, v+1):
            if not vst[e] and adj[s][e]:
                stk.append(s)

                s=e
                vst[s]=1
                alst.append(s)
                break
        else: # 더이상 연결된 방문노드가 없는 경우
            if stk:
                s=stk.pop() # 스택에서 꺼낸 가장 최근 데이터가 기준점이 된다.
            else:
                break       # 탐색할 위치가 스택에 없음.

# 인접 행렬을 통해 트리의 연결상태를 표현.
# 파이썬은 인접 리스트도 가능함. 반면 다른 언어는 인접 행렬만 가능함.

T = int(input())

for tc in range(1, 1+T):
    v, e = map(int, input().split())
    
    
    인접행렬에 연결표시
    adj = [[0]*(v+1) for _ in range(v+1)]
    for _ in range(e):
        st,ed = map(int, input().split())
        adj[st][ed]=adj[ed][st]=1
    
    alst = []
    dfs_stk(1)
    print(f'#{tc}', *alst)
