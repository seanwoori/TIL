import sys
sys.stdin = open('input.txt', 'r')

def dfs(s):
    for e in adj[s]:        # 나와 연결된
        if v[e]==0:         # 만약 e가 방문되지 않았다면,
            v[e]=1          # 방문체크, v[e]=1
            # v[e]=1을 통해, 방문한 노드는 재귀호출을 하지 않음. 매우 중요한 라인
            alst.append(e)  # 빈 행렬에 e append
            dfs(e)          # 위에까지 단위작업.

T = int(input())
for tc in range(1, 1+T):
    V, E = map(int, input().split()) # V:vertex, E: edge

    # [1] 연결리스트에 연결표시(append)
    adj = [[] for _ in range(V+1)]
    for _ in range(E):
        s,e=map(int, input().split()) # 시작 노드, 끝 노드
        adj[s].append(e)
        adj[e].append(s)

    # adj를 오름차순으로 정렬 필요 !
    for i in range(1, 1+V):
        adj[i].sort()

    alst=[]
    v = [0]+(V+1)
    # 시작지점은 방문표시
    v[1]=1
    alst.append(1)
    dfs(1)
    print(f'#{tc}', alst)
'''
[2] stack을 이용한 풀이

def dfs(s):
    stk=[]

    while True:
        for e in adj[s]:    # s에 연결된 노드를 방문
            if v[e]==0:     # 미방문
                # 정답처리
                if e==G:
                    return 1
                stk.append(s)
                s=e
                v[s]=1
                break
        else:               # 더이상 탐색할 노드가 없는 경우=>직전으로 돌아감
            if stk:
                s=stk.pop()
            else:
                break
        return 0

T = int(input())
for tc in range(1, 1+T):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int, input().split())
        adj[s].append(e)

    S, G = map(int, input().split())
    v = [0]*(V+1)
    ans = dfs(S)
    print(f'#{tc} {ans}')
'''